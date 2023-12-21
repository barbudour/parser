# ValidationKey - класс
Ключ сообщения о результате валидации. Позволяет определить причину сообщения.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Validation](N_Tessa_Platform_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class ValidationKey : RegistryItem<Guid, ValidationKey>
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class ValidationKey
    	Inherits RegistryItem(Of Guid, ValidationKey)
C++ __Копировать
    [SerializableAttribute]
    public ref class ValidationKey sealed : public RegistryItem<Guid, ValidationKey^>
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type ValidationKey = 
        class
            inherit RegistryItem<Guid, ValidationKey>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[RegistryItem](T_Tessa_Platform_RegistryItem_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid), ValidationKey> __ ValidationKey
##  __Конструкторы
[ValidationKey](M_Tessa_Platform_Validation_ValidationKey__ctor.htm)|  Создаёт
экземпляр класса с указанием свойств ключа сообщения о результате валидации.  
---|---  
## __Свойства
[ID](P_Tessa_Platform_RegistryItem_2_ID.htm)| Идентификатор объекта, по
которому выполняется регистрация в реестре.  
(Унаследован от [RegistryItem<TIdentifier,
TItem>](T_Tessa_Platform_RegistryItem_2.htm))  
---|---  
[Message](P_Tessa_Platform_Validation_ValidationKey_Message.htm)|  Сообщение,
связанное с ключом валидации, или null, если такое сообщение отсутствует.  
[Name](P_Tessa_Platform_RegistryItem_2_Name.htm)| Имя объекта, по которому
объект можно идентифицировать в коллекциях.  
(Унаследован от [RegistryItem<TIdentifier,
TItem>](T_Tessa_Platform_RegistryItem_2.htm))  
[Registry](P_Tessa_Platform_Validation_ValidationKey_Registry.htm)| Реестр,
содержащий все зарегистрированные типы.  
(Переопределяет [RegistryItem<TIdentifier,
TItem>.Registry](P_Tessa_Platform_RegistryItem_2_Registry.htm))  
##  __Методы
[Equals(Object)](M_Tessa_Platform_RegistryItem_2_Equals.htm)| Сравнивает
текущий объект с заданным.  
(Унаследован от [RegistryItem<TIdentifier,
TItem>](T_Tessa_Platform_RegistryItem_2.htm))  
---|---  
[Equals(TItem)](M_Tessa_Platform_RegistryItem_2_Equals_1.htm)| Сравнивает
текущий объект с заданным.  
(Унаследован от [RegistryItem<TIdentifier,
TItem>](T_Tessa_Platform_RegistryItem_2.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FromGuid](M_Tessa_Platform_Validation_ValidationKey_FromGuid.htm)|
Возвращает тип по уникальному идентификатору, полученному посредством метода
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
[Unknown](F_Tessa_Platform_Validation_ValidationKey_Unknown.htm)|  Неизвестный
ключ сообщения о результате валидации по умолчанию. Используется в случае,
если для сообщения не был явно задан ключ.  
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
[Tessa.Platform.Validation - пространство
имён](N_Tessa_Platform_Validation.htm)
