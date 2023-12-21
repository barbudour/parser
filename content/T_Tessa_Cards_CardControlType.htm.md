# CardControlType - класс
Тип элемента управления, используемый в объектах метаинформации по типу
карточки [CardType](T_Tessa_Cards_CardType.htm) для связи с пользовательским
интерфейсом редактирования карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class CardControlType : RegistryItem<Guid, CardControlType>
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class CardControlType
    	Inherits RegistryItem(Of Guid, CardControlType)
C++ __Копировать
    [SerializableAttribute]
    public ref class CardControlType sealed : public RegistryItem<Guid, CardControlType^>
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type CardControlType = 
        class
            inherit RegistryItem<Guid, CardControlType>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[RegistryItem](T_Tessa_Platform_RegistryItem_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid), CardControlType> __ CardControlType
##  __Конструкторы
[CardControlType](M_Tessa_Cards_CardControlType__ctor.htm)|  Создаёт экземпляр
типа с указанием идентификатора и имени типа элемента управления.  
---|---  
## __Свойства
[Flags](P_Tessa_Cards_CardControlType_Flags.htm)|  Флаги элемента управления,
описывающие его поведение.  
---|---  
[ID](P_Tessa_Platform_RegistryItem_2_ID.htm)| Идентификатор объекта, по
которому выполняется регистрация в реестре.  
(Унаследован от [RegistryItem<TIdentifier,
TItem>](T_Tessa_Platform_RegistryItem_2.htm))  
[IsUnknown](P_Tessa_Cards_CardControlType_IsUnknown.htm)|  Признак того, что
тип элемента управления неизвестен системе.  
[Name](P_Tessa_Platform_RegistryItem_2_Name.htm)| Имя объекта, по которому
объект можно идентифицировать в коллекциях.  
(Унаследован от [RegistryItem<TIdentifier,
TItem>](T_Tessa_Platform_RegistryItem_2.htm))  
[Registry](P_Tessa_Cards_CardControlType_Registry.htm)| Реестр, содержащий все
зарегистрированные типы.  
(Переопределяет [RegistryItem<TIdentifier,
TItem>.Registry](P_Tessa_Platform_RegistryItem_2_Registry.htm))  
[UsageMode](P_Tessa_Cards_CardControlType_UsageMode.htm)|  Способ
использования элемента управления.  
## __Методы
[CreateUnknown](M_Tessa_Cards_CardControlType_CreateUnknown.htm)|  Создаёт
объект, который неизвестен в реестре, т.е. возвращает
[IsUnknown](P_Tessa_Cards_CardControlType_IsUnknown.htm), равный true.  
---|---  
[Equals(Object)](M_Tessa_Platform_RegistryItem_2_Equals.htm)| Сравнивает
текущий объект с заданным.  
(Унаследован от [RegistryItem<TIdentifier,
TItem>](T_Tessa_Platform_RegistryItem_2.htm))  
[Equals(TItem)](M_Tessa_Platform_RegistryItem_2_Equals_1.htm)| Сравнивает
текущий объект с заданным.  
(Унаследован от [RegistryItem<TIdentifier,
TItem>](T_Tessa_Platform_RegistryItem_2.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FromGuid](M_Tessa_Cards_CardControlType_FromGuid.htm)|  Возвращает тип по
уникальному идентификатору, полученному посредством метода
[Tessa.Platform.RegistryItem{TItem}.ToGuid].  
[GetHashCode](M_Tessa_Platform_RegistryItem_2_GetHashCode.htm)| Возвращает
хеш-код объекта.  
(Унаследован от [RegistryItem<TIdentifier,
TItem>](T_Tessa_Platform_RegistryItem_2.htm))  
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
(Унаследован от [RegistryItem<TIdentifier,
TItem>](T_Tessa_Platform_RegistryItem_2.htm))  
[ToName](M_Tessa_Platform_RegistryItem_2_ToName.htm)|  Преобразует тип в
уникальное имя, по которому можно будет восстановить исходный тип. Для
восстановления по имени используйте метод [FromName<T>(INamedRegistry<T>,
String)](M_Tessa_Platform_RegistryItem_2_FromName__1.htm). Не следует
использовать метод для объектов, имя которых может быть неуникальным.  
(Унаследован от [RegistryItem<TIdentifier,
TItem>](T_Tessa_Platform_RegistryItem_2.htm))  
[ToString](M_Tessa_Platform_RegistryItem_2_ToString.htm)| Возвращает строковое
представление объекта.  
(Унаследован от [RegistryItem<TIdentifier,
TItem>](T_Tessa_Platform_RegistryItem_2.htm))  
##  __Поля
[UnknownName](F_Tessa_Cards_CardControlType_UnknownName.htm)|  Тип элемента
управления, который не был найден в реестре типов.  
---|---  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
