# Registry<TIdentifier, TItem> \- класс
Потокобезопасный реестр объектов, идентифицируемых по
[Guid](https://learn.microsoft.com/dotnet/api/system.guid).
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class Registry<TIdentifier, TItem> : IRegistry<TIdentifier, TItem>
    where TItem : Object, IRegistryItem<TIdentifier>
VB __Копировать
     Public MustInherit Class Registry(Of TIdentifier, TItem As {Object, IRegistryItem(Of TIdentifier)})
    	Implements IRegistry(Of TIdentifier, TItem)
C++ __Копировать
    generic<typename TIdentifier, typename TItem>
    where TItem : Object, IRegistryItem<TIdentifier>
    public ref class Registry abstract : IRegistry<TIdentifier, TItem>
F# __Копировать
     [<AbstractClassAttribute>]
    type Registry<'TIdentifier, 'TItem when 'TItem : Object and IRegistryItem<'TIdentifier>> = 
        class
            interface IRegistry<'TIdentifier, 'TItem>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ Registry<TIdentifier, TItem>
Derived
[Tessa.Cards.CardControlTypeRegistry](T_Tessa_Cards_CardControlTypeRegistry.htm)
[Tessa.Cards.CardTypeExtensionTypeRegistry](T_Tessa_Cards_CardTypeExtensionTypeRegistry.htm)
[Tessa.Cards.CardValidatorTypeRegistry](T_Tessa_Cards_CardValidatorTypeRegistry.htm)
[Tessa.Cards.Numbers.NumberEventTypeRegistry](T_Tessa_Cards_Numbers_NumberEventTypeRegistry.htm)
[Tessa.Cards.Numbers.NumberLocationTypeRegistry](T_Tessa_Cards_Numbers_NumberLocationTypeRegistry.htm)
[Tessa.Cards.Numbers.NumberQueueActionTypeRegistry](T_Tessa_Cards_Numbers_NumberQueueActionTypeRegistry.htm)
[Tessa.Cards.Numbers.NumberQueueEventTypeRegistry](T_Tessa_Cards_Numbers_NumberQueueEventTypeRegistry.htm)
[Tessa.Cards.Numbers.NumberQueuePredicateTypeRegistry](T_Tessa_Cards_Numbers_NumberQueuePredicateTypeRegistry.htm)
[Tessa.Cards.Workflow.WorkflowQueueEventTypeRegistry](T_Tessa_Cards_Workflow_WorkflowQueueEventTypeRegistry.htm)
[Tessa.Cards.Workflow.WorkflowSignalTypeRegistry](T_Tessa_Cards_Workflow_WorkflowSignalTypeRegistry.htm)
[Tessa.Extensions.Platform.Server.Cards.Satellites.SatelliteTypeRegistry](T_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeRegistry.htm)
[Tessa.Platform.NamedRegistry<T>](T_Tessa_Platform_NamedRegistry_1.htm)
[Tessa.Platform.Placeholders.PlaceholderValueTypeRegistry](T_Tessa_Platform_Placeholders_PlaceholderValueTypeRegistry.htm)
[Tessa.Platform.Runtime.ActionTypeRegistry](T_Tessa_Platform_Runtime_ActionTypeRegistry.htm)
[Tessa.UI.Workflow.WorkflowEngineTileManagerUIExtensionRegistry](T_Tessa_UI_Workflow_WorkflowEngineTileManagerUIExtensionRegistry.htm)
[Tessa.UI.WorkflowViewer.Actions.WorkflowActionUIHandlerRegistry](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerRegistry.htm)
[Tessa.Workflow.Actions.WorkflowActionRegistry](T_Tessa_Workflow_Actions_WorkflowActionRegistry.htm)
[Tessa.Workflow.WorkflowEngineTileManagerExtensionRegistry](T_Tessa_Workflow_WorkflowEngineTileManagerExtensionRegistry.htm)
Подробнее __Less __
Implements
    [IRegistry](T_Tessa_Platform_IRegistry_2.htm)<TIdentifier, TItem>
#### Параметры типа
TIdentifier
     Тип уникального идентификатора, по которому сравниваются объекта. Обычно это [Guid](https://learn.microsoft.com/dotnet/api/system.guid) или [Int32](https://learn.microsoft.com/dotnet/api/system.int32). 
TItem
     Тип объектов, содержащихся в реестре и реализующих интерфейс [IRegistryItem<TIdentifier>](T_Tessa_Platform_IRegistryItem_1.htm). 
## __Конструкторы
[Registry<TIdentifier, TItem>](M_Tessa_Platform_Registry_2__ctor.htm)|
Инициализирует новый экземпляр класса Registry<TIdentifier, TItem>  
---|---  
##  __Методы
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
[Get](M_Tessa_Platform_Registry_2_Get.htm)| Возвращает объект,
зарегистрированный в реестре по заданному идентификатору.  
[GetAll](M_Tessa_Platform_Registry_2_GetAll.htm)| Возвращает все
зарегистрированные в реестре объекты.  
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
[IsDefined(TIdentifier)](M_Tessa_Platform_Registry_2_IsDefined.htm)|
Возвращает признак того, что в реестре был зарегистрирован объект по заданному
идентификатору.  
[IsDefined(TItem)](M_Tessa_Platform_Registry_2_IsDefined_1.htm)| Возвращает
признак того, что заданный объект был зарегистрирован в реестре.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Register](M_Tessa_Platform_Registry_2_Register.htm)| Регистрирует объект по
его идентификатору. Метод замещает предыдущую регистрацию при её наличии.  
[RegisterCore](M_Tessa_Platform_Registry_2_RegisterCore.htm)| Регистрирует
объект по его идентификатору. Метод замещает предыдущую регистрацию при её
наличии.  
[RegisterNew](M_Tessa_Platform_Registry_2_RegisterNew.htm)|  Регистрирует
новый объект в реестре. Если элемент уже присутствует, то никаких действий не
производится.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGet](M_Tessa_Platform_Registry_2_TryGet.htm)|  Возвращает объект в
параметре result, зарегистрированный в реестре по заданному идентификатору.
Метод возвращает false, если объект отсутствует в реестре.  
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
