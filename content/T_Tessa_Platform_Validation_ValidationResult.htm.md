# ValidationResult - класс
Результат валидации. Экземпляры класса являются неизменяемыми.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Validation](N_Tessa_Platform_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class ValidationResult : IEquatable<ValidationResult>, 
    	IFormattable, ISerializable, ISealable, IBinarySerializable, IBsonSerializable, 
    	IJsonSerializable
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class ValidationResult
    	Implements IEquatable(Of ValidationResult), IFormattable, 
    	ISerializable, ISealable, IBinarySerializable, IBsonSerializable, IJsonSerializable
C++ __Копировать
    [SerializableAttribute]
    public ref class ValidationResult sealed : IEquatable<ValidationResult^>, 
    	IFormattable, ISerializable, ISealable, IBinarySerializable, IBsonSerializable, 
    	IJsonSerializable
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type ValidationResult = 
        class
            interface IEquatable<ValidationResult>
            interface IFormattable
            interface ISerializable
            interface ISealable
            interface IBinarySerializable
            interface IBsonSerializable
            interface IJsonSerializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ValidationResult
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<ValidationResult>, [IFormattable](https://learn.microsoft.com/dotnet/api/system.iformattable), [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable), [IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm), [IBsonSerializable](T_Tessa_Platform_IBsonSerializable.htm), [IJsonSerializable](T_Tessa_Platform_IJsonSerializable.htm), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Заметки
Для сериализации объекта ValidationResult посредством
[DataContractSerializer](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.datacontractserializer)
следует добавить тип класса ValidationResult и тип массива
[ValidationResultItem](T_Tessa_Platform_Validation_ValidationResultItem.htm)[]
в список известных типов
[KnownTypes](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.datacontractserializer.knowntypes#system-
runtime-serialization-datacontractserializer-knowntypes).
## __Конструкторы
[ValidationResult()](M_Tessa_Platform_Validation_ValidationResult__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
Устарело.  
---|---  
[ValidationResult(IEnumerable<ValidationResultItem>)](M_Tessa_Platform_Validation_ValidationResult__ctor_1.htm)|
Создаёт экземпляр класса с указанием сообщений, возникших при валидации.  
## __Свойства
[Empty](P_Tessa_Platform_Validation_ValidationResult_Empty.htm)|  Пустой
результат валидации.  
---|---  
[HasErrors](P_Tessa_Platform_Validation_ValidationResult_HasErrors.htm)|
Признак того, что результаты валидации содержат сообщения об ошибках.  
[HasInfo](P_Tessa_Platform_Validation_ValidationResult_HasInfo.htm)|  Признак
того, что результаты валидации содержат информационные сообщения.  
[HasWarnings](P_Tessa_Platform_Validation_ValidationResult_HasWarnings.htm)|
Признак того, что результаты валидации содержат предупреждения.  
[IsSealed](P_Tessa_Platform_Validation_ValidationResult_IsSealed.htm)| Признак
того, что объект был защищён от изменений.  
[IsSuccessful](P_Tessa_Platform_Validation_ValidationResult_IsSuccessful.htm)|
Признак того, что валидации завершилась успехом.  
[Items](P_Tessa_Platform_Validation_ValidationResult_Items.htm)|  Сообщения,
возникшие при валидации.  
## __Методы
[Aggregate(ValidationResult[])](M_Tessa_Platform_Validation_ValidationResult_Aggregate_1.htm)|
Выполняет объединение результатов валидации. Возвращаемый результат
гарантированно не равен null.  
---|---  
[Aggregate(ValidationResult,
ValidationResult)](M_Tessa_Platform_Validation_ValidationResult_Aggregate.htm)|
Выполняет объединение результатов валидации. Возвращаемый результат
гарантированно не равен null.  
[ConvertToSuccessful](M_Tessa_Platform_Validation_ValidationResult_ConvertToSuccessful.htm)|
Преобразует текущий результат валидации в успешный, в котором все ошибки
заменяются на предупреждения, или возвращает текущий объект, если в нём нет
сообщений-ошибок.  
[Deserialize](M_Tessa_Platform_Validation_ValidationResult_Deserialize.htm)|
Десериализует объект из бинарной формы.  
[Equals(Object)](M_Tessa_Platform_Validation_ValidationResult_Equals.htm)|
Сравнивает текущий объект с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Equals(ValidationResult)](M_Tessa_Platform_Validation_ValidationResult_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
[Equals(ValidationResult,
ValidationResult)](M_Tessa_Platform_Validation_ValidationResult_Equals_2.htm)|
Сравнивает объекты ValidationResult.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FromException(Exception,
Boolean)](M_Tessa_Platform_Validation_ValidationResult_FromException.htm)|
Возвращает результат валидации для исключения. Возвращаемый объект не равен
null.  
[FromException(Object, Exception, Boolean, String,
String)](M_Tessa_Platform_Validation_ValidationResult_FromException_1.htm)|
Возвращает результат валидации для исключения. Возвращаемый объект не равен
null.  
[FromText(String,
ValidationResultType)](M_Tessa_Platform_Validation_ValidationResult_FromText_1.htm)|
Возвращает результат валидации для текста сообщения. Возвращаемый объект не
равен null.  
[FromText(Object, String,
ValidationResultType)](M_Tessa_Platform_Validation_ValidationResult_FromText.htm)|
Возвращает результат валидации для текста сообщения. Возвращаемый объект не
равен null.  
[GetHashCode](M_Tessa_Platform_Validation_ValidationResult_GetHashCode.htm)|
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
[Seal](M_Tessa_Platform_Validation_ValidationResult_Seal.htm)| Защищает объект
от изменений.  
[Serialize](M_Tessa_Platform_Validation_ValidationResult_Serialize.htm)|
Сериализует объект в бинарной форме.  
[ToPlain](M_Tessa_Platform_Validation_ValidationResult_ToPlain.htm)|
Преобразует текущий объект в простую сериализуемую форму
[PlainValidationResult](T_Tessa_Platform_Validation_PlainValidationResult.htm).
Созданный объект можно отправить любому сериализатору, в т.ч.
нетипизированному JSON-сериализатору, и получить на выходе тот же объект,
преобразуемый в ValidationResult вызовом метода
[ToValidationResult()](M_Tessa_Platform_Validation_PlainValidationResult_ToValidationResult.htm).  
[ToString()](M_Tessa_Platform_Validation_ValidationResult_ToString.htm)|
Возвращает строковое представление объекта, включающее подробную информацию о
событиях валидации.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
[ToString(String)](M_Tessa_Platform_Validation_ValidationResult_ToString_1.htm)|
Возвращает строковое представление объекта с использованием информации о
форматировании для текущей культуры.  
[ToString(ValidationLevel)](M_Tessa_Platform_Validation_ValidationResult_ToString_3.htm)|
Возвращает текстовое представление для сообщений валидации с указанным режимом
вывода.  
[ToString(String,
IFormatProvider)](M_Tessa_Platform_Validation_ValidationResult_ToString_2.htm)|
Возвращает строковое представление объекта с использованием информации о
форматировании.  
##  __Операторы
[Addition(ValidationResult,
ValidationResult)](M_Tessa_Platform_Validation_ValidationResult_op_Addition.htm)|
Складывает два значения и возвращает их сумму.  
---|---  
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
