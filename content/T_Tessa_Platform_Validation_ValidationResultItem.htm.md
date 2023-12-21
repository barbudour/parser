# ValidationResultItem - класс
Сообщение о валидации.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Validation](N_Tessa_Platform_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class ValidationResultItem : IFormattable, 
    	IValidationResultItem, IEquatable<IValidationResultItem>
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class ValidationResultItem
    	Implements IFormattable, IValidationResultItem, IEquatable(Of IValidationResultItem)
C++ __Копировать
    [SerializableAttribute]
    public ref class ValidationResultItem sealed : IFormattable, 
    	IValidationResultItem, IEquatable<IValidationResultItem^>
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type ValidationResultItem = 
        class
            interface IFormattable
            interface IValidationResultItem
            interface IEquatable<IValidationResultItem>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ValidationResultItem
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IValidationResultItem](T_Tessa_Platform_Validation_IValidationResultItem.htm)>, [IFormattable](https://learn.microsoft.com/dotnet/api/system.iformattable), [IValidationResultItem](T_Tessa_Platform_Validation_IValidationResultItem.htm)
##  __Конструкторы
[ValidationResultItem(IValidationResultItem, Nullable<ValidationResultType>,
Boolean)](M_Tessa_Platform_Validation_ValidationResultItem__ctor.htm)|
Создаёт экземпляр класса копированием свойств из заданного объекта,
содержащего сообщение о валидации.  
---|---  
[ValidationResultItem(ValidationKey, ValidationResultType, String, String,
String, String,
String)](M_Tessa_Platform_Validation_ValidationResultItem__ctor_1.htm)|
Создаёт экземпляр класса с указанием текста и типа сообщения, возникшего при
валидации.  
## __Свойства
[Details](P_Tessa_Platform_Validation_ValidationResultItem_Details.htm)|
Дополнительная информация о сообщении, например, полный текст исключения, или
null, если дополнительная информация отсутствует.  
---|---  
[FieldName](P_Tessa_Platform_Validation_ValidationResultItem_FieldName.htm)|
Имя поля объекта, к которому относится сообщение валидации, или null, если
поле неизвестно.  
[Key](P_Tessa_Platform_Validation_ValidationResultItem_Key.htm)| Ключ
сообщения, возникшего при валидации.  
[Message](P_Tessa_Platform_Validation_ValidationResultItem_Message.htm)| Текст
сообщения, возникшего при валидации.  
[ObjectName](P_Tessa_Platform_Validation_ValidationResultItem_ObjectName.htm)|
Имя объекта, к которому относится сообщение валидации, или null, если имя
неизвестно.  
[ObjectType](P_Tessa_Platform_Validation_ValidationResultItem_ObjectType.htm)|
Тип объекта, к которому относится сообщение валидации, или null, если тип
неизвестен.  
[Type](P_Tessa_Platform_Validation_ValidationResultItem_Type.htm)| Тип
сообщения, возникшего при валидации.  
##  __Методы
[CalculateHashCode](M_Tessa_Platform_Validation_ValidationResultItem_CalculateHashCode.htm)|
Возвращает хеш-код заданного элемента.  
---|---  
[Deserialize](M_Tessa_Platform_Validation_ValidationResultItem_Deserialize.htm)|
Десериализует объект из бинарной формы.  
[Equals(IValidationResultItem)](M_Tessa_Platform_Validation_ValidationResultItem_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
[Equals(Object)](M_Tessa_Platform_Validation_ValidationResultItem_Equals.htm)|
Сравнивает текущий объект с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Equals(IValidationResultItem,
IValidationResultItem)](M_Tessa_Platform_Validation_ValidationResultItem_Equals_2.htm)|
Сравнивает сообщения валидации по всем свойствам.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Platform_Validation_ValidationResultItem_GetHashCode.htm)|
Возвращает хеш-код объекта.  
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
[Serialize](M_Tessa_Platform_Validation_ValidationResultItem_Serialize.htm)|
Сериализует объект в бинарной форме.  
[ToString()](M_Tessa_Platform_Validation_ValidationResultItem_ToString.htm)|
Возвращает строковое представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
[ToString(IValidationResultItem)](M_Tessa_Platform_Validation_ValidationResultItem_ToString_3.htm)|
Возвращает текстовое представление по умолчанию для заданного сообщения о
валидации.  
[ToString(String)](M_Tessa_Platform_Validation_ValidationResultItem_ToString_1.htm)|
Возвращает строковое представление объекта с использованием информации о
форматировании для текущей культуры.  
[ToString(ValidationLevel)](M_Tessa_Platform_Validation_ValidationResultItem_ToString_4.htm)|
Возвращает текстовое представление для сообщения валидации с указанным режимом
вывода.  
[ToString(String,
IFormatProvider)](M_Tessa_Platform_Validation_ValidationResultItem_ToString_2.htm)|
Возвращает строковое представление объекта с использованием информации о
форматировании.  
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
[Tessa.Platform.Validation - пространство
имён](N_Tessa_Platform_Validation.htm)
