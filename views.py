import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee


@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            if Employee.objects.filter(eid=data['eid']).exists():
                return JsonResponse({'error': 'Employee ID already exists'}, status=400)

            employee = Employee(
                eid=data['eid'],
                ename=data['ename'],
                ecity=data.get('ecity', ''),
                edept=data.get('edept', ''),
                esal=data['esal'],
                erole=data['erole']
            )

            employee.set_password(data['epassword'])
            employee.save()

            return JsonResponse({'message': 'Employee registered successfully'})

        except Exception:
            return JsonResponse({'error': 'Something went wrong'}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            employee = Employee.objects.filter(eid=data['eid']).first()

            if employee and employee.check_password(data['epassword']):
                return JsonResponse({
                    'message': 'Login successful',
                    'eid': employee.eid
                })

            return JsonResponse({'error': 'Invalid credentials'}, status=400)

        except Exception:
            return JsonResponse({'error': 'Something went wrong'}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


def profile(request, eid):
    if request.method == 'GET':
        try:
            employee = Employee.objects.get(eid=eid)

            data = {
                'eid': employee.eid,
                'ename': employee.ename,
                'ecity': employee.ecity,
                'edept': employee.edept,
                'esal': employee.esal,
                'erole': employee.erole,
                'bio': employee.bio,
                'education': employee.education,
                'skills': employee.skills,
            }

            return JsonResponse(data)

        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee not found'}, status=404)

    return JsonResponse({'error': 'Method not allowed'}, status=405)