# CardValidatorType - класс
Тип валидатора, используемый в объектах метаинформации по типу карточки
[CardType](T_Tessa_Cards_CardType.htm) для связи с пользовательским
интерфейсом редактирования карточки и с валидацией карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class CardValidatorType : RegistryItem<Guid, CardValidatorType>
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class CardValidatorType
    	Inherits RegistryItem(Of Guid, CardValidatorType)
C++ __Копировать
    [SerializableAttribute]
    public ref class CardValidatorType sealed : public RegistryItem<Guid, CardValidatorType^>
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type CardValidatorType = 
        class
            inherit RegistryItem<Guid, CardValidatorType>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[RegistryItem](T_Tessa_Platform_RegistryItem_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid), CardValidatorType> __ CardValidatorType
##  __Конструкторы
[CardValidatorType(Guid, String)](M_Tessa_Cards_CardValidatorType__ctor.htm)|
Создаёт экземпляр типа с заданными идентификатором и именем.  
---|---  
[CardValidatorType(Guid, String, CardValidationMode[],
CardInstanceType[])](M_Tessa_Cards_CardValidatorType__ctor_1.htm)|  Создаёт
экземпляр типа с заданными идентификатором и именем.  
## __Свойства
[ID](P_Tessa_Platform_RegistryItem_2_ID.htm)| Идентификатор объекта, по
которому выполняется регистрация в реестре.  
(Унаследован от [RegistryItem<TIdentifier,
TItem>](T_Tessa_Platform_RegistryItem_2.htm))  
---|---  
[IsUnknown](P_Tessa_Cards_CardValidatorType_IsUnknown.htm)|  Признак того, что
тип элемента управления неизвестен системе.  
[Name](P_Tessa_Platform_RegistryItem_2_Name.htm)| Имя объекта, по которому
объект можно идентифицировать в коллекциях.  
(Унаследован от [RegistryItem<TIdentifier,
TItem>](T_Tessa_Platform_RegistryItem_2.htm))  
[Registry](P_Tessa_Cards_CardValidatorType_Registry.htm)| Реестр, содержащий
все зарегистрированные типы.  
(Переопределяет [RegistryItem<TIdentifier,
TItem>.Registry](P_Tessa_Platform_RegistryItem_2_Registry.htm))  
##  __Методы
[CreateUnknown](M_Tessa_Cards_CardValidatorType_CreateUnknown.htm)|  Создаёт
объект, который неизвестен в реестре, т.е. возвращает
[IsUnknown](P_Tessa_Cards_CardValidatorType_IsUnknown.htm), равный true.  
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
[FromGuid](M_Tessa_Cards_CardValidatorType_FromGuid.htm)|  Возвращает тип по
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
[IsAllowed(CardInstanceType)](M_Tessa_Cards_CardValidatorType_IsAllowed.htm)|
Возвращает признак того, что валидатор разрешён для заданного типа экземпляра
карточки.  
[IsAllowed(CardValidationMode)](M_Tessa_Cards_CardValidatorType_IsAllowed_1.htm)|
Возвращает признак того, что валидатор разрешён для заданного способа
выполнения валидации.  
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
[UnknownName](F_Tessa_Cards_CardValidatorType_UnknownName.htm)|  Тип
валидатора, который не был найден в реестре типов.  
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
