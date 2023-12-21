# ClientConditionRepairManager - класс
Менеджер починки условий на клиенте.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Conditions](N_Tessa_Platform_Conditions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ClientConditionRepairManager : ConditionRepairManagerBase
VB __Копировать
     Public NotInheritable Class ClientConditionRepairManager
    	Inherits ConditionRepairManagerBase
C++ __Копировать
     public ref class ClientConditionRepairManager sealed : public ConditionRepairManagerBase
F# __Копировать
     [<SealedAttribute>]
    type ClientConditionRepairManager = 
        class
            inherit ConditionRepairManagerBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ConditionRepairManagerBase](T_Tessa_Platform_Conditions_ConditionRepairManagerBase.htm) __ ClientConditionRepairManager
##  __Конструкторы
[ClientConditionRepairManager](M_Tessa_Platform_Conditions_ClientConditionRepairManager__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
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
[RepairConditionsAsync](M_Tessa_Platform_Conditions_ConditionRepairManagerBase_RepairConditionsAsync.htm)|
Выполняет починку условий в карточке.  
(Унаследован от
[ConditionRepairManagerBase](T_Tessa_Platform_Conditions_ConditionRepairManagerBase.htm))  
[RepairConditionsCoreAsync](M_Tessa_Platform_Conditions_ConditionRepairManagerBase_RepairConditionsCoreAsync.htm)|
Выполняет починку условий в карточке.  
(Унаследован от
[ConditionRepairManagerBase](T_Tessa_Platform_Conditions_ConditionRepairManagerBase.htm))  
[RepairConditionTypesAsync](M_Tessa_Platform_Conditions_ConditionRepairManagerBase_RepairConditionTypesAsync.htm)|
Выполняет починку условий для указанных типов условий во всех карточках.  
(Унаследован от
[ConditionRepairManagerBase](T_Tessa_Platform_Conditions_ConditionRepairManagerBase.htm))  
[RepairConditionTypesCoreAsync](M_Tessa_Platform_Conditions_ClientConditionRepairManager_RepairConditionTypesCoreAsync.htm)|
Выполняет починку условий для указанных типов условий во всех карточках.  
(Переопределяет
[ConditionRepairManagerBase.RepairConditionTypesCoreAsync(ICollection<Guid>,
CancellationToken)](M_Tessa_Platform_Conditions_ConditionRepairManagerBase_RepairConditionTypesCoreAsync.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[CardMetadata](F_Tessa_Platform_Conditions_ConditionRepairManagerBase_CardMetadata.htm)|  
(Унаследован от
[ConditionRepairManagerBase](T_Tessa_Platform_Conditions_ConditionRepairManagerBase.htm))  
---|---  
[CardRepairManager](F_Tessa_Platform_Conditions_ConditionRepairManagerBase_CardRepairManager.htm)|  
(Унаследован от
[ConditionRepairManagerBase](T_Tessa_Platform_Conditions_ConditionRepairManagerBase.htm))  
[ConditionTypesParameterKey](F_Tessa_Platform_Conditions_ClientConditionRepairManager_ConditionTypesParameterKey.htm)|
Ключ, по которому указываются идентификаторы типов условий для починки при
отправке запроса на сервер.  
[ConditionTypesProvider](F_Tessa_Platform_Conditions_ConditionRepairManagerBase_ConditionTypesProvider.htm)|  
(Унаследован от
[ConditionRepairManagerBase](T_Tessa_Platform_Conditions_ConditionRepairManagerBase.htm))  
[HandlerResolver](F_Tessa_Platform_Conditions_ConditionRepairManagerBase_HandlerResolver.htm)|  
(Унаследован от
[ConditionRepairManagerBase](T_Tessa_Platform_Conditions_ConditionRepairManagerBase.htm))  
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
