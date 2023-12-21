# ConditionRepairManagerBase - класс
Базовая реализация менеджера починки условий, которая содержит общие для
клиента и сервера методы.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Conditions](N_Tessa_Platform_Conditions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ConditionRepairManagerBase : IConditionRepairManager
VB __Копировать
     Public MustInherit Class ConditionRepairManagerBase
    	Implements IConditionRepairManager
C++ __Копировать
     public ref class ConditionRepairManagerBase abstract : IConditionRepairManager
F# __Копировать
     [<AbstractClassAttribute>]
    type ConditionRepairManagerBase = 
        class
            interface IConditionRepairManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConditionRepairManagerBase
Derived
[Tessa.Platform.Conditions.ClientConditionRepairManager](T_Tessa_Platform_Conditions_ClientConditionRepairManager.htm)
[Tessa.Platform.Conditions.ConditionRepairManager](T_Tessa_Platform_Conditions_ConditionRepairManager.htm)
Implements
    [IConditionRepairManager](T_Tessa_Platform_Conditions_IConditionRepairManager.htm)
##  __Конструкторы
[ConditionRepairManagerBase](M_Tessa_Platform_Conditions_ConditionRepairManagerBase__ctor.htm)|
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
[RepairConditionsCoreAsync](M_Tessa_Platform_Conditions_ConditionRepairManagerBase_RepairConditionsCoreAsync.htm)|
Выполняет починку условий в карточке.  
[RepairConditionTypesAsync](M_Tessa_Platform_Conditions_ConditionRepairManagerBase_RepairConditionTypesAsync.htm)|
Выполняет починку условий для указанных типов условий во всех карточках.  
[RepairConditionTypesCoreAsync](M_Tessa_Platform_Conditions_ConditionRepairManagerBase_RepairConditionTypesCoreAsync.htm)|
Выполняет починку условий для указанных типов условий во всех карточках.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[CardMetadata](F_Tessa_Platform_Conditions_ConditionRepairManagerBase_CardMetadata.htm)|  
---|---  
[CardRepairManager](F_Tessa_Platform_Conditions_ConditionRepairManagerBase_CardRepairManager.htm)|  
[ConditionTypesProvider](F_Tessa_Platform_Conditions_ConditionRepairManagerBase_ConditionTypesProvider.htm)|  
[HandlerResolver](F_Tessa_Platform_Conditions_ConditionRepairManagerBase_HandlerResolver.htm)|  
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
[Tessa.Platform.Conditions - пространство
имён](N_Tessa_Platform_Conditions.htm)
