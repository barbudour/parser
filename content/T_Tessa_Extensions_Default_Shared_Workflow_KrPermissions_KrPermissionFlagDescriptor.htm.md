# KrPermissionFlagDescriptor - класс
Объект, содержащий информацию о текущем флаге настроек прав доступа
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public class KrPermissionFlagDescriptor : IEquatable<KrPermissionFlagDescriptor>
VB __Копировать
     Public Class KrPermissionFlagDescriptor
    	Implements IEquatable(Of KrPermissionFlagDescriptor)
C++ __Копировать
     public ref class KrPermissionFlagDescriptor : IEquatable<KrPermissionFlagDescriptor^>
F# __Копировать
     type KrPermissionFlagDescriptor = 
        class
            interface IEquatable<KrPermissionFlagDescriptor>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrPermissionFlagDescriptor
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<KrPermissionFlagDescriptor>
##  __Конструкторы
[KrPermissionFlagDescriptor(Guid, String,
KrPermissionFlagDescriptor[])](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor__ctor_1.htm)|
Объект, содержащий информацию о текущем флаге настроек прав доступа, не
харящийся в базе данных и не имеющий контрола в карточке прав доступа.  
---|---  
[KrPermissionFlagDescriptor(Guid, String, Int32, String, String, String,
String,
KrPermissionFlagDescriptor[])](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor__ctor.htm)|
Объект, содержащий информацию о текущем флаге настроек прав доступа  
## __Свойства
[ControlCaption](P_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor_ControlCaption.htm)|
Имя контрола флага в карточке правил доступа.  
---|---  
[ControlTooltip](P_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor_ControlTooltip.htm)|
Подсказка к контролу флага в карточке правил доступа.  
[Description](P_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor_Description.htm)|
Описание флага. Выводится в ообщения о правах на карточку или когда
недостаточно прав  
[ID](P_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor_ID.htm)|
Идентификатор флага  
[IncludedPermissions](P_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor_IncludedPermissions.htm)|
Список флагов, которые включает текущий флаг  
[IsVirtual](P_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor_IsVirtual.htm)|
Определяет, что данный флаг виртуальный и его не нужно проверять по базе  
[Name](P_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor_Name.htm)|
Имя флага  
[Order](P_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor_Order.htm)|
Порядковый номер флага. Определяет расположение флагов в карточке правила
доступа. Данное свойство можно изменить, чтобы переопределить порядок
стандартных флагов. Делать это следует на этапе регистрации объектов.  
[SqlName](P_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor_SqlName.htm)|
Имя поля в SQL в таблице KrPermissions. Если не задано, то флаг не хранится в
базе  
## __Методы
[Equals(KrPermissionFlagDescriptor)](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor_Equals_1.htm)|  
---|---  
[Equals(Object)](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor_Equals.htm)|  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor_GetHashCode.htm)|  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor_ToString.htm)|  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
##  __Операторы
[Equality(KrPermissionFlagDescriptor,
Guid)](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor_op_Equality.htm)|  
---|---  
[Equality(KrPermissionFlagDescriptor,
KrPermissionFlagDescriptor)](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor_op_Equality_1.htm)|  
[Inequality(KrPermissionFlagDescriptor,
Guid)](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor_op_Inequality.htm)|  
[Inequality(KrPermissionFlagDescriptor,
KrPermissionFlagDescriptor)](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor_op_Inequality_1.htm)|  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)
