# FieldsConditionSourceHandlerBase - класс
Обработчик источника данных, получающий и сохраняющий настройки условий
напрямую из секции карточки.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Conditions](N_Tessa_Platform_Conditions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class FieldsConditionSourceHandlerBase : IConditionSourceHandler
VB __Копировать
     Public MustInherit Class FieldsConditionSourceHandlerBase
    	Implements IConditionSourceHandler
C++ __Копировать
     public ref class FieldsConditionSourceHandlerBase abstract : IConditionSourceHandler
F# __Копировать
     [<AbstractClassAttribute>]
    type FieldsConditionSourceHandlerBase = 
        class
            interface IConditionSourceHandler
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FieldsConditionSourceHandlerBase
Derived
[Tessa.Extensions.Default.Shared.Conditions.KrPermissionsConditionSourceHandler](T_Tessa_Extensions_Default_Shared_Conditions_KrPermissionsConditionSourceHandler.htm)
[Tessa.Extensions.Default.Shared.Conditions.KrSecondaryProcessConditionSourceHandler](T_Tessa_Extensions_Default_Shared_Conditions_KrSecondaryProcessConditionSourceHandler.htm)
[Tessa.Extensions.Default.Shared.Conditions.KrVirtualFileConditionSourceHandler](T_Tessa_Extensions_Default_Shared_Conditions_KrVirtualFileConditionSourceHandler.htm)
Implements
    [IConditionSourceHandler](T_Tessa_Platform_Conditions_IConditionSourceHandler.htm)
##  __Конструкторы
[FieldsConditionSourceHandlerBase](M_Tessa_Platform_Conditions_FieldsConditionSourceHandlerBase__ctor.htm)|
Создаёт экземпляр класса с указанием его свойств.  
---|---  
## __Свойства
[DbScope](P_Tessa_Platform_Conditions_FieldsConditionSourceHandlerBase_DbScope.htm)|
Объект для взаимодействия с базой данных. Может быть не задан, если обработчик
используется на клиентской стороне.  
---|---  
[FieldName](P_Tessa_Platform_Conditions_FieldsConditionSourceHandlerBase_FieldName.htm)|
Имя поля, где хранятся настройки условий.  
[SectionName](P_Tessa_Platform_Conditions_FieldsConditionSourceHandlerBase_SectionName.htm)|
Имя секции, где хранятся настройки условий.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetCardIDsWithConditionAsync](M_Tessa_Platform_Conditions_FieldsConditionSourceHandlerBase_GetCardIDsWithConditionAsync.htm)|
Возвращает список идентификаторов карточек, соответствующий данному
обработчику, в которых есть условия с заданным в conditionTypeID типом
условия. Если тип условия не задан, то возвращает все идентификаторы карточек,
в которых есть условия.  
[GetConditionSources](M_Tessa_Platform_Conditions_FieldsConditionSourceHandlerBase_GetConditionSources.htm)|
Возвращает коллекцию источников данных для условий из карточки.  
[GetCustomSourceCardNameAsync](M_Tessa_Platform_Conditions_FieldsConditionSourceHandlerBase_GetCustomSourceCardNameAsync.htm)|
Возвращает имя кастомное имя карточки-источника условий, если оно отличается
от дайджеста карточки. Если метод возвращает null, то в качестве имени
карточки-источника используется её дайджест.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
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
[Tessa.Platform.Conditions - пространство
имён](N_Tessa_Platform_Conditions.htm)
