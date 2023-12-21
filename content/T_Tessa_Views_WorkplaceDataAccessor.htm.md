# WorkplaceDataAccessor - класс
Акссесор для получения моделей рабочих мест из БД
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WorkplaceDataAccessor
VB __Копировать
     Public NotInheritable Class WorkplaceDataAccessor
C++ __Копировать
     public ref class WorkplaceDataAccessor sealed
F# __Копировать
     [<SealedAttribute>]
    type WorkplaceDataAccessor = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkplaceDataAccessor
##  __Конструкторы
[WorkplaceDataAccessor](M_Tessa_Views_WorkplaceDataAccessor__ctor.htm)|
Initializes a new instance of the WorkplaceDataAccessor class.  
---|---  
## __Методы
[ChangeWorkplaceAsync](M_Tessa_Views_WorkplaceDataAccessor_ChangeWorkplaceAsync.htm)|
Осуществляет обновление информации о рабочих местах  
---|---  
[ClearAsync](M_Tessa_Views_WorkplaceDataAccessor_ClearAsync.htm)|
Осуществляет очистку справочника рабочих мест  
[DeleteWorkplaceAsync](M_Tessa_Views_WorkplaceDataAccessor_DeleteWorkplaceAsync.htm)|
Удаляет информацию о рабочих местах  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetClientWorkplacesAsync](M_Tessa_Views_WorkplaceDataAccessor_GetClientWorkplacesAsync.htm)|
Возвращает список рабочих мест для клиентских приложений. Доступные рабочие
места ограничиваются наличием доступных разрешений. В том числе и для
администраторов. Администратору будут доступны рабочие места с нулевым
количеством заданных ролей, либо с явно указанными ролями в которые входит
администратор  
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
[GetWorkplacesAsync](M_Tessa_Views_WorkplaceDataAccessor_GetWorkplacesAsync.htm)|
Возвращает список моделей рабочих мест доступных текущему пользователю.  
[ImportWorkplacesAsync](M_Tessa_Views_WorkplaceDataAccessor_ImportWorkplacesAsync.htm)|
Осуществляет импорт рабочих мест  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[StoreWorkplaceAsync](M_Tessa_Views_WorkplaceDataAccessor_StoreWorkplaceAsync.htm)|
Осуществляет сохранение рабочих мест в БД. [имен рабочих
мест](P_Tessa_Views_Workplaces_WorkplaceModel_Name.htm)  
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
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
