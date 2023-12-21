# Validator - класс
Объект, осуществляющий валидацию свойств.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Validation](N_Tessa_Platform_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class Validator : IDisposable, 
    	ISealable
VB __Копировать
     Public NotInheritable Class Validator
    	Implements IDisposable, ISealable
C++ __Копировать
     public ref class Validator sealed : IDisposable, 
    	ISealable
F# __Копировать
     [<SealedAttribute>]
    type Validator = 
        class
            interface IDisposable
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ Validator
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[IsSealed](P_Tessa_Platform_Validation_Validator_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
---|---  
##  __Методы
[Dispose](M_Tessa_Platform_Validation_Validator_Dispose.htm)| Освобождает
ресурсы, занимаемые объектом.  
---|---  
[End](M_Tessa_Platform_Validation_Validator_End.htm)|  Возвращает объект
валидации в пул. Его нельзя использовать до момента следующего получения из
пула через
[ValidationSequence](T_Tessa_Platform_Validation_ValidationSequence.htm).
Метод возвращает объект
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm),
для которого была создана последовательность валидации.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Error(ValidationKey)](M_Tessa_Platform_Validation_Validator_Error.htm)|
Добавляет сообщение об ошибке валидации с указанным ключом. Используется текст
сообщения, заданный в ключе.  
[Error(ValidationKey,
Object[])](M_Tessa_Platform_Validation_Validator_Error_1.htm)|  Добавляет
сообщение об ошибке валидации с указанными ключом и параметрами. Используется
шаблон сообщения, заданный в ключе.  
[ErrorDetails(String,
Exception)](M_Tessa_Platform_Validation_Validator_ErrorDetails.htm)|
Добавляет сообщение об ошибке валидации с указанными текстом и дополнительной
информацией по заданному исключению. Ключ сообщения принимается как
неизвестный.  
[ErrorDetails(String,
String)](M_Tessa_Platform_Validation_Validator_ErrorDetails_1.htm)|  Добавляет
сообщение об ошибке валидации с указанными текстом и дополнительной
информацией. Ключ сообщения принимается как неизвестный.  
[ErrorDetails(ValidationKey,
String)](M_Tessa_Platform_Validation_Validator_ErrorDetails_2.htm)|  Добавляет
сообщение об ошибке валидации с указанными ключом и дополнительной
информацией. Используется текст сообщения, заданный в ключе.  
[ErrorDetails(ValidationKey, String,
Exception)](M_Tessa_Platform_Validation_Validator_ErrorDetails_3.htm)|
Добавляет сообщение об ошибке валидации с указанными ключом, текстом и
дополнительной информацией по заданному исключению.  
[ErrorDetails(ValidationKey, String,
String)](M_Tessa_Platform_Validation_Validator_ErrorDetails_4.htm)|  Добавляет
сообщение об ошибке валидации с указанными ключом, текстом и дополнительной
информацией.  
[ErrorException(Exception, String,
String)](M_Tessa_Platform_Validation_Validator_ErrorException.htm)|  Добавляет
сообщение об ошибке с указанием возникшего исключения. Ключ сообщения
принимается как неизвестный. Исключение
[AggregateException](https://learn.microsoft.com/dotnet/api/system.aggregateexception)
преобразуется в несколько сообщений для каждого агрегированного исключения.  
[ErrorException(ValidationKey, Exception, String,
String)](M_Tessa_Platform_Validation_Validator_ErrorException_1.htm)|
Добавляет сообщение об ошибке с указанием ключа сообщения и возникшего
исключения. Исключение
[AggregateException](https://learn.microsoft.com/dotnet/api/system.aggregateexception)
преобразуется в несколько сообщений для каждого агрегированного исключения.  
[ErrorText(String)](M_Tessa_Platform_Validation_Validator_ErrorText.htm)|
Добавляет сообщение об ошибке валидации с указанным текстом. Ключ сообщения
принимается как неизвестный.  
[ErrorText(String,
Object[])](M_Tessa_Platform_Validation_Validator_ErrorText_1.htm)|  Добавляет
сообщение об ошибке валидации с указанными шаблоном сообщения и параметрами.
Ключ сообщения принимается как неизвестный.  
[ErrorText(ValidationKey,
String)](M_Tessa_Platform_Validation_Validator_ErrorText_2.htm)|  Добавляет
сообщение об ошибке валидации с указанными ключом и текстом.  
[ErrorText(ValidationKey, String,
Object[])](M_Tessa_Platform_Validation_Validator_ErrorText_3.htm)|  Добавляет
сообщение об ошибке валидации с указанными ключом, шаблоном сообщения и
параметрами.  
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
[Info(ValidationKey)](M_Tessa_Platform_Validation_Validator_Info.htm)|
Добавляет информационное сообщение о валидации с указанным ключом.
Используется текст сообщения, заданный в ключе.  
[Info(ValidationKey,
Object[])](M_Tessa_Platform_Validation_Validator_Info_1.htm)|  Добавляет
информационное сообщение о валидации с указанными ключом и параметрами.
Используется шаблон сообщения, заданный в ключе.  
[InfoDetails(String,
Exception)](M_Tessa_Platform_Validation_Validator_InfoDetails.htm)|  Добавляет
информационное сообщение о валидации с указанными текстом и дополнительной
информацией по заданному исключению. Ключ сообщения принимается как
неизвестный.  
[InfoDetails(String,
String)](M_Tessa_Platform_Validation_Validator_InfoDetails_1.htm)|  Добавляет
информационное сообщение о валидации с указанными текстом и дополнительной
информацией. Ключ сообщения принимается как неизвестный.  
[InfoDetails(ValidationKey,
String)](M_Tessa_Platform_Validation_Validator_InfoDetails_2.htm)|  Добавляет
информационное сообщение о валидации с указанными ключом и дополнительной
информацией. Используется текст сообщения, заданный в ключе.  
[InfoDetails(ValidationKey, String,
Exception)](M_Tessa_Platform_Validation_Validator_InfoDetails_3.htm)|
Добавляет информационное сообщение о валидации с указанными ключом, текстом и
дополнительной информацией по заданному исключению.  
[InfoDetails(ValidationKey, String,
String)](M_Tessa_Platform_Validation_Validator_InfoDetails_4.htm)|  Добавляет
информационное сообщение о валидации с указанными ключом, текстом и
дополнительной информацией.  
[InfoException(Exception, String,
String)](M_Tessa_Platform_Validation_Validator_InfoException.htm)|  Добавляет
информационное сообщение о возникшем исключении. Ключ сообщения принимается
как неизвестный. Исключение
[AggregateException](https://learn.microsoft.com/dotnet/api/system.aggregateexception)
преобразуется в несколько сообщений для каждого агрегированного исключения.  
[InfoException(ValidationKey, Exception, String,
String)](M_Tessa_Platform_Validation_Validator_InfoException_1.htm)|
Добавляет информационное сообщение о возникшем исключении с указанным ключом.
Исключение
[AggregateException](https://learn.microsoft.com/dotnet/api/system.aggregateexception)
преобразуется в несколько сообщений для каждого агрегированного исключения.  
[InfoText(String)](M_Tessa_Platform_Validation_Validator_InfoText.htm)|
Добавляет информационное сообщение о валидации с указанным текстом. Ключ
сообщения принимается как неизвестный.  
[InfoText(String,
Object[])](M_Tessa_Platform_Validation_Validator_InfoText_1.htm)|  Добавляет
информационное сообщение о валидации с указанными шаблоном сообщения и
параметрами. Ключ сообщения принимается как неизвестный.  
[InfoText(ValidationKey,
String)](M_Tessa_Platform_Validation_Validator_InfoText_2.htm)|  Добавляет
информационное сообщение о валидации с указанными ключом и текстом.  
[InfoText(ValidationKey, String,
Object[])](M_Tessa_Platform_Validation_Validator_InfoText_3.htm)|  Добавляет
информационное сообщение о валидации с указанными ключом, шаблоном сообщения и
параметрами.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Message](M_Tessa_Platform_Validation_Validator_Message.htm)|  Добавляет
сообщение о валидации с указанием типа, ключа валидации, подробностей,
информационного поля и параметров сообщения.  
[Seal](M_Tessa_Platform_Validation_Validator_Seal.htm)| Защищает объект от
изменений.  
[SetMessage(ValidationKey)](M_Tessa_Platform_Validation_Validator_SetMessage.htm)|
Изменяет ключ сообщения, выдаваемого в процессе валидации. Тип сообщения
остаётся прежним.  
[SetMessage(ValidationKey,
ValidationResultType)](M_Tessa_Platform_Validation_Validator_SetMessage_1.htm)|
Изменяет ключ и тип сообщения, выдаваемого в процессе валидации.  
[SetObjectName(String)](M_Tessa_Platform_Validation_Validator_SetObjectName_1.htm)|
Изменяет имя объекта, валидация которого выполняется. Тип объекта остаётся
прежним.  
[SetObjectName(Object,
String)](M_Tessa_Platform_Validation_Validator_SetObjectName.htm)|
Устанавливает имя объекта, валидация которого выполняется, в соответствии с
именем заданного типа.  
[SetObjectName(Type,
String)](M_Tessa_Platform_Validation_Validator_SetObjectName_2.htm)|
Устанавливает имя объекта, валидация которого выполняется, в соответствии с
именем заданного типа.  
[SetResult](M_Tessa_Platform_Validation_Validator_SetResult.htm)|  Изменяет
тип сообщения, выдаваемого в процессе валидации. Ключ и шаблон сообщения
остаются прежними.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Validate(IValidationObject)](M_Tessa_Platform_Validation_Validator_Validate_2.htm)|
Осуществляет валидацию заданного объекта validationObject.  
[Validate(String,
Func<Boolean>)](M_Tessa_Platform_Validation_Validator_Validate.htm)|
Осуществляет валидацию некоторого условия для свойства с заданным именем
fieldName и возвращает объект валидации Validator.  
[Validate(String, Func<String,
Boolean>)](M_Tessa_Platform_Validation_Validator_Validate_1.htm)|
Осуществляет валидацию некоторого условия для свойства с заданным именем
fieldName и возвращает объект валидации Validator.  
[Validate<T>(String, T, Func<T,
Boolean>)](M_Tessa_Platform_Validation_Validator_Validate__1_2.htm)|
Осуществляет валидацию условия для свойства с заданным именем fieldName и
значением fieldValue, и возвращает объект валидации Validator.  
[Validate<T>(String, Func<T, Boolean>, Func<String, Func<T, Boolean>,
Boolean>)](M_Tessa_Platform_Validation_Validator_Validate__1_1.htm)|
Осуществляет валидацию свойства с заданным именем fieldName и типом T и
возвращает объект валидации Validator.  
[Validate<T>(String, Func<T>, Func<T, Boolean>, Func<String, Func<T>, Func<T,
Boolean>, Boolean>)](M_Tessa_Platform_Validation_Validator_Validate__1.htm)|
Осуществляет валидацию свойства заданного через fieldGetter свойства, имеющего
тип T, и возвращает объект валидации Validator.  
[ValidateMany(IEnumerable<IValidationObject>)](M_Tessa_Platform_Validation_Validator_ValidateMany.htm)|
Осуществляет валидацию всех объектов в заданном перечислении
validationObjects.  
[ValidateMany<TKey, TValue>(IDictionary<TKey,
TValue>)](M_Tessa_Platform_Validation_Validator_ValidateMany__2.htm)|
Осуществляет валидацию всех объектов-значений в заданной коллекции пар ключ /
значение.  
[ValidateMany<TKey, TValue>(String, Func<IDictionary<TKey, TValue>>,
Func<TValue,
Boolean>)](M_Tessa_Platform_Validation_Validator_ValidateMany__2_1.htm)|
Осуществляет валидацию всех объектов-значений в коллекции пар ключ / значение
посредством заданной функции valueIsValid.  
[ValidateUnique<TObject,
TValue>](M_Tessa_Platform_Validation_Validator_ValidateUnique__2.htm)|
Проверяет на уникальность все объекты в заданной коллекции. Если найдены
объекты с одинаковыми значениями уникальных свойств, то в объект валидации
добавляется сообщение с параметрами, установленными методом
[SetMessage(ValidationKey,
ValidationResultType)](M_Tessa_Platform_Validation_Validator_SetMessage_1.htm),
(или аналогичными методами), причём в качестве аргументов передаются: {0} \-
имя первого неуникального объекта; {1} \- имя второго неуникального объекта;
{2} \- значение первого неуникального объекта; {3} \- значение второго
неуникального объекта.  
[Warning(ValidationKey)](M_Tessa_Platform_Validation_Validator_Warning.htm)|
Добавляет сообщение с предупреждением о валидации с указанным ключом. Ключ
сообщения принимается как неизвестный.  
[Warning(ValidationKey,
Object[])](M_Tessa_Platform_Validation_Validator_Warning_1.htm)|  Добавляет
сообщение с предупреждением о валидации с указанными ключом и параметрами.
Используется шаблон сообщения, заданный в ключе.  
[WarningDetails(String,
Exception)](M_Tessa_Platform_Validation_Validator_WarningDetails.htm)|
Добавляет сообщение с предупреждением о валидации с указанными текстом и
дополнительной информацией по заданному исключению. Ключ сообщения принимается
как неизвестный.  
[WarningDetails(String,
String)](M_Tessa_Platform_Validation_Validator_WarningDetails_1.htm)|
Добавляет сообщение с предупреждением о валидации с указанными текстом и
дополнительной информацией. Ключ сообщения принимается как неизвестный.  
[WarningDetails(ValidationKey,
String)](M_Tessa_Platform_Validation_Validator_WarningDetails_2.htm)|
Добавляет сообщение с предупреждением о валидации с указанными ключом и
дополнительной информацией. Используется текст сообщения, заданный в ключе.  
[WarningDetails(ValidationKey, String,
Exception)](M_Tessa_Platform_Validation_Validator_WarningDetails_3.htm)|
Добавляет сообщение с предупреждением о валидации с указанными ключом, текстом
и дополнительной информацией по заданному исключению.  
[WarningDetails(ValidationKey, String,
String)](M_Tessa_Platform_Validation_Validator_WarningDetails_4.htm)|
Добавляет сообщение с предупреждением о валидации с указанными ключом, текстом
и дополнительной информацией.  
[WarningException(Exception, String,
String)](M_Tessa_Platform_Validation_Validator_WarningException.htm)|
Добавляет сообщение с предупреждением о возникшем исключении. Ключ сообщения
принимается как неизвестный. Исключение
[AggregateException](https://learn.microsoft.com/dotnet/api/system.aggregateexception)
преобразуется в несколько сообщений для каждого агрегированного исключения.  
[WarningException(ValidationKey, Exception, String,
String)](M_Tessa_Platform_Validation_Validator_WarningException_1.htm)|
Добавляет сообщение с предупреждением о возникшем исключении с указанным
ключом. Исключение
[AggregateException](https://learn.microsoft.com/dotnet/api/system.aggregateexception)
преобразуется в несколько сообщений для каждого агрегированного исключения.  
[WarningText(String)](M_Tessa_Platform_Validation_Validator_WarningText.htm)|
Добавляет сообщение с предупреждением о валидации с указанным текстом. Ключ
сообщения принимается как неизвестный.  
[WarningText(String,
Object[])](M_Tessa_Platform_Validation_Validator_WarningText_1.htm)|
Добавляет сообщение с предупреждением о валидации с указанными шаблоном
сообщения и параметрами. Ключ сообщения принимается как неизвестный.  
[WarningText(ValidationKey,
String)](M_Tessa_Platform_Validation_Validator_WarningText_2.htm)|  Добавляет
сообщение с предупреждением о валидации с указанными ключом и текстом.  
[WarningText(ValidationKey, String,
Object[])](M_Tessa_Platform_Validation_Validator_WarningText_3.htm)|
Добавляет сообщение с предупреждением о валидации с указанными ключом,
шаблоном сообщения и параметрами.  
## __Методы расширения
[ConvertToValidationItem](M_Tessa_Views_Validation_ViewMetadataValidatorHelper_ConvertToValidationItem.htm)|
Пробразует ошибку кода в результат валидации codeError  
(Определяется
[ViewMetadataValidatorHelper](T_Tessa_Views_Validation_ViewMetadataValidatorHelper.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[InvalidContext](M_Tessa_Views_Validation_ViewMetadataValidatorHelper_InvalidContext.htm)|
Добавляет сообщение об ошибке валидации с ключем
[InvalidContext](F_Tessa_Views_Validation_ViewValidationKeys_InvalidContext.htm)  
(Определяется
[ViewMetadataValidatorHelper](T_Tessa_Views_Validation_ViewMetadataValidatorHelper.htm))  
[InvalidTextInMetadata](M_Tessa_Views_Validation_ViewMetadataValidatorHelper_InvalidTextInMetadata.htm)|
Добавляет сообщение об ошибке валидации с ключем
[InvalidTextInMetadata](F_Tessa_Views_Validation_ViewValidationKeys_InvalidTextInMetadata.htm)  
(Определяется
[ViewMetadataValidatorHelper](T_Tessa_Views_Validation_ViewMetadataValidatorHelper.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[UnknownKeyword](M_Tessa_Views_Validation_ViewMetadataValidatorHelper_UnknownKeyword.htm)|
Добавляет сообщение об ошибке валидации с ключем
[UnknownKeyword](F_Tessa_Views_Validation_ViewValidationKeys_UnknownKeyword.htm)  
(Определяется
[ViewMetadataValidatorHelper](T_Tessa_Views_Validation_ViewMetadataValidatorHelper.htm))  
[UnknownMetadataParameter](M_Tessa_Views_Validation_ViewMetadataValidatorHelper_UnknownMetadataParameter.htm)|
Добавляет сообщение об ошибке валидации с ключем
[UnknownMetadataParameter](F_Tessa_Views_Validation_ViewValidationKeys_UnknownMetadataParameter.htm)  
(Определяется
[ViewMetadataValidatorHelper](T_Tessa_Views_Validation_ViewMetadataValidatorHelper.htm))  
[ValidateAppearances](M_Tessa_Views_Validation_ViewMetadataValidatorHelper_ValidateAppearances.htm)|
Осуществляет проверку корректности заполнения метаданных внешнего вида
элементов метаданных  
(Определяется
[ViewMetadataValidatorHelper](T_Tessa_Views_Validation_ViewMetadataValidatorHelper.htm))  
[ValidateColumns](M_Tessa_Views_Validation_ViewMetadataValidatorHelper_ValidateColumns.htm)|
Осуществляет проверку корректности заполнения столбцов и ссылок на столбцы в
метаданных представления  
(Определяется
[ViewMetadataValidatorHelper](T_Tessa_Views_Validation_ViewMetadataValidatorHelper.htm))  
[ValidateExtensions](M_Tessa_Views_Validation_ViewMetadataValidatorHelper_ValidateExtensions.htm)|
Осуществляет проверку корректности заполнения метаданных расширений  
(Определяется
[ViewMetadataValidatorHelper](T_Tessa_Views_Validation_ViewMetadataValidatorHelper.htm))  
[ValidateParameters](M_Tessa_Views_Validation_ViewMetadataValidatorHelper_ValidateParameters.htm)|
Осуществляет проверку корректности заполнения параметров представлений  
(Определяется
[ViewMetadataValidatorHelper](T_Tessa_Views_Validation_ViewMetadataValidatorHelper.htm))  
[ValidateReferences](M_Tessa_Views_Validation_ViewMetadataValidatorHelper_ValidateReferences.htm)|
Осуществляет проверку корректности заполнения метаданных ссылочных секций  
(Определяется
[ViewMetadataValidatorHelper](T_Tessa_Views_Validation_ViewMetadataValidatorHelper.htm))  
[ValidateSubsets](M_Tessa_Views_Validation_ViewMetadataValidatorHelper_ValidateSubsets.htm)|
Осуществляет проверку подмножеств  
(Определяется
[ViewMetadataValidatorHelper](T_Tessa_Views_Validation_ViewMetadataValidatorHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Validation - пространство
имён](N_Tessa_Platform_Validation.htm)
