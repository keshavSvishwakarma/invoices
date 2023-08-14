from rest_framework.test import APITestCase
from rest_framework import status
from .models import Invoice, InvoiceDetail

class InvoiceAPITestCase(APITestCase):
    def setUp(self):
        self.invoice_data = {
            'date': '2023-08-14',
            'invoice_no': 'INV123',
            'customer_name': 'John Doe',
            'invoice_details': [  # This is a list of detail dictionaries
                {
                    'description': 'Item 1',
                    'quantity': 2,
                    'unit_price': 10.00
                },
                {
                    'description': 'Item 2',
                    'quantity': 1,
                    'unit_price': 20.00
                }
            ]
        }
    # def test_create_invoice(self):
    #     response = self.client.post('/invoices/', self.invoice_data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Invoice.objects.count(), 1)
    #     self.assertEqual(InvoiceDetail.objects.count(), 2)

    # def test_get_invoices(self):
    #     Invoice.objects.create(date='2023-08-14', invoice_no='INV124', customer_name='Jane Smith')
    #     response = self.client.get('/invoices/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 1)

    # def test_get_single_invoice(self):
    #     invoice = Invoice.objects.create(date='2023-08-14', invoice_no='INV125', customer_name='Alice Johnson')
    #     response = self.client.get(f'/invoices/{invoice.id}/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['invoice_no'], 'INV125')
