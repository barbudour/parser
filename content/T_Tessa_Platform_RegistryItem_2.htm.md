# RegistryItem<TIdentifier, TItem> \- класс
Базовый класс для реализации интерфейса
[IRegistryItem<TIdentifier>](T_Tessa_Platform_IRegistryItem_1.htm), а также
для указания строкового представления объекта
[INamedItem](T_Tessa_Platform_Collections_INamedItem.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public abstract class RegistryItem<TIdentifier, TItem> : IEquatable<TItem>, 
    	INamedItem, IRegistryItem<TIdentifier>
    where TItem : RegistryItem<TIdentifier, TItem>
VB __Копировать
    <SerializableAttribute>
    Public MustInherit Class RegistryItem(Of TIdentifier, TItem As RegistryItem(Of TIdentifier, TItem))
    	Implements IEquatable(Of TItem), INamedItem, IRegistryItem(Of TIdentifier)
C++ __Копировать
    [SerializableAttribute]
    generic<typename TIdentifier, typename TItem>
    where TItem : RegistryItem<TIdentifier, TItem>
    public ref class RegistryItem abstract : IEquatable<TItem>, 
    	INamedItem, IRegistryItem<TIdentifier>
F# __Копировать
     [<AbstractClassAttribute>]
    [<SerializableAttribute>]
    type RegistryItem<'TIdentifier, 'TItem when 'TItem : RegistryItem<'TIdentifier, 'TItem>> = 
        class
            interface IEquatable<'TItem>
            interface INamedItem
            interface IRegistryItem<'TIdentifier>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RegistryItem<TIdentifier, TItem>
Derived
[Tessa.Cards.CardControlType](T_Tessa_Cards_CardControlType.htm)
[Tessa.Cards.CardTypeExtensionType](T_Tessa_Cards_CardTypeExtensionType.htm)
[Tessa.Cards.CardValidatorType](T_Tessa_Cards_CardValidatorType.htm)
[Tessa.Cards.Numbers.NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)
[Tessa.Cards.Numbers.NumberLocationType](T_Tessa_Cards_Numbers_NumberLocationType.htm)
[Tessa.Cards.Numbers.NumberQueueActionType](T_Tessa_Cards_Numbers_NumberQueueActionType.htm)
[Tessa.Cards.Numbers.NumberQueueEventType](T_Tessa_Cards_Numbers_NumberQueueEventType.htm)
[Tessa.Cards.Numbers.NumberQueuePredicateType](T_Tessa_Cards_Numbers_NumberQueuePredicateType.htm)
[Tessa.Cards.Numbers.NumberType](T_Tessa_Cards_Numbers_NumberType.htm)
[Tessa.Cards.Workflow.WorkflowQueueEventType](T_Tessa_Cards_Workflow_WorkflowQueueEventType.htm)
[Tessa.Cards.Workflow.WorkflowSignalType](T_Tessa_Cards_Workflow_WorkflowSignalType.htm)
[Tessa.Platform.Placeholders.PlaceholderValueType](T_Tessa_Platform_Placeholders_PlaceholderValueType.htm)
[Tessa.Platform.Runtime.ActionType](T_Tessa_Platform_Runtime_ActionType.htm)
[Tessa.Platform.Validation.ValidationKey](T_Tessa_Platform_Validation_ValidationKey.htm)
Подробнее __Less __
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<TItem>, [INamedItem](T_Tessa_Platform_Collections_INamedItem.htm), [IRegistryItem](T_Tessa_Platform_IRegistryItem_1.htm)<TIdentifier>
#### Параметры типа
TIdentifier
     Тип уникального идентификатора, по которому сравниваются объекта. Обычно это [Guid](https://learn.microsoft.com/dotnet/api/system.guid) или [Int32](https://learn.microsoft.com/dotnet/api/system.int32). 
TItem
     Тип реализуемого объекта, т.е. тип, унаследованный от абстрактного класса. 
## __Конструкторы
[RegistryItem<TIdentifier, TItem>](M_Tessa_Platform_RegistryItem_2__ctor.htm)|
Создаёт экземпляр типа с заданными идентификатором и именем.  
---|---  
##  __Свойства
[ID](P_Tessa_Platform_RegistryItem_2_ID.htm)| Идентификатор объекта, по
которому выполняется регистрация в реестре.  
---|---  
[Name](P_Tessa_Platform_RegistryItem_2_Name.htm)| Имя объекта, по которому
объект можно идентифицировать в коллекциях.  
[Registry](P_Tessa_Platform_RegistryItem_2_Registry.htm)| Реестр, содержащий
все зарегистрированные типы.  
##  __Методы
[Equals(Object)](M_Tessa_Platform_RegistryItem_2_Equals.htm)| Сравнивает
текущий объект с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
---|---  
[Equals(TItem)](M_Tessa_Platform_RegistryItem_2_Equals_1.htm)| Сравнивает
текущий объект с заданным.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FromIdentifier](M_Tessa_Platform_RegistryItem_2_FromIdentifier.htm)|
Возвращает тип по уникальному идентификатору, полученному посредством метода
[ToIdentifier()](M_Tessa_Platform_RegistryItem_2_ToIdentifier.htm).  
[FromName<T>](M_Tessa_Platform_RegistryItem_2_FromName__1.htm)|  Возвращает
тип по уникальному имени, полученному посредством метода
[ToName()](M_Tessa_Platform_RegistryItem_2_ToName.htm).  
[GetHashCode](M_Tessa_Platform_RegistryItem_2_GetHashCode.htm)| Возвращает
хеш-код объекта.  
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
[ToIdentifier](M_Tessa_Platform_RegistryItem_2_ToIdentifier.htm)|  Преобразует
тип в уникальный идентификатор, по которому можно будет восстановить исходный
тип. Для восстановления по идентификатору используйте метод
[FromIdentifier(IRegistry<TIdentifier, TItem>,
TIdentifier)](M_Tessa_Platform_RegistryItem_2_FromIdentifier.htm).  
[ToName](M_Tessa_Platform_RegistryItem_2_ToName.htm)|  Преобразует тип в
уникальное имя, по которому можно будет восстановить исходный тип. Для
восстановления по имени используйте метод [FromName<T>(INamedRegistry<T>,
String)](M_Tessa_Platform_RegistryItem_2_FromName__1.htm). Не следует
использовать метод для объектов, имя которых может быть неуникальным.  
[ToString](M_Tessa_Platform_RegistryItem_2_ToString.htm)| Возвращает строковое
представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
##  __Операторы
[Equality(RegistryItem<TIdentifier, TItem>, RegistryItem<TIdentifier,
TItem>)](M_Tessa_Platform_RegistryItem_2_op_Equality.htm)| Сравнивает заданные
значения на равенство.  
---|---  
[Inequality(RegistryItem<TIdentifier, TItem>, RegistryItem<TIdentifier,
TItem>)](M_Tessa_Platform_RegistryItem_2_op_Inequality.htm)| Сравнивает
заданные значения на неравенство.  
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
