
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from pyExcelerator import *
from StringIO import StringIO

def export_as_xls(modeladmin, request, queryset):
    """
    Generic xls export admin action.
    """
    if not request.user.is_staff:
        raise PermissionDenied
    opts = modeladmin.model._meta
    
    wb = Workbook()
    ws0 = wb.add_sheet('0')
    col = 0
    field_names = []
    # write header row
    for field in opts.fields:
        ws0.write(0, col, field.name)
        field_names.append(field.name)
        col = col + 1
    
    row = 1
    # Write data rows
    for obj in queryset:
        col = 0
        for field in field_names:
            val = unicode(getattr(obj, field)).strip()
            ws0.write(row, col, val)
            col = col + 1
        row = row + 1	

	f = StringIO()
	wb.save(f)
	f.seek(0)
	response = HttpResponse(f.read(), mimetype='application/ms-excel')
    # response['Content-Disposition'] = 'attachment; filename=%s.xls' % unicode(opts).replace('.', '_')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % unicode('exportar')
    return response
    
export_as_xls.short_description = "Exportar a Microsoft Excel"
