# Tessa.Platform.Validation - пространство имён
Вспомогательные классы для выполнения валидации.
##  __Классы
[FakeValidationResultBuilder](T_Tessa_Platform_Validation_FakeValidationResultBuilder.htm)|
Игнорирует все сообщения о валидации, но корректно отображает признак того,
что валидация выполнена успешно
[IsSuccessful()](M_Tessa_Platform_Validation_FakeValidationResultBuilder_IsSuccessful.htm),
а также гарантирует, что объект, возвращённый методом
[Build(Boolean)](M_Tessa_Platform_Validation_FakeValidationResultBuilder_Build.htm),
будет иметь такое же значение
[IsSuccessful](P_Tessa_Platform_Validation_ValidationResult_IsSuccessful.htm).  
---|---  
[NameValidationHelper](T_Tessa_Platform_Validation_NameValidationHelper.htm)|  
[PlainValidationResult](T_Tessa_Platform_Validation_PlainValidationResult.htm)|
Объект, свойства которого соответствуют элементу
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm), удобный
для сериализации.  
[PlainValidationResultItem](T_Tessa_Platform_Validation_PlainValidationResultItem.htm)|
Объект, свойства которого соответствуют элементу
[IValidationResultItem](T_Tessa_Platform_Validation_IValidationResultItem.htm),
удобный для сериализации.  
[ValidateThat](T_Tessa_Platform_Validation_ValidateThat.htm)|  Предикаты для
процесса валидации.  
[ValidationException](T_Tessa_Platform_Validation_ValidationException.htm)|
Ошибка, связанная с результатом валидации
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm).  
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm)|
Методы-расширения для классов валидации.  
[ValidationInfoStorageObject](T_Tessa_Platform_Validation_ValidationInfoStorageObject.htm)|
Строго типизированный декоратор для хранилища IDictionary<string, object>,
поддерживающий валидацию свойств и расширение произвольными данными через
свойство Info.  
[ValidationKey](T_Tessa_Platform_Validation_ValidationKey.htm)|  Ключ
сообщения о результате валидации. Позволяет определить причину сообщения.  
[ValidationKeyRegistry](T_Tessa_Platform_Validation_ValidationKeyRegistry.htm)|
Реестр ключей валидации
[ValidationKey](T_Tessa_Platform_Validation_ValidationKey.htm). Класс является
синглтоном.  
[ValidationKeys](T_Tessa_Platform_Validation_ValidationKeys.htm)|  Стандартные
ключи валидации.  
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm)|  Объект,
поддерживающий валидацию свойств.  
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)|
Результат валидации. Экземпляры класса являются неизменяемыми.  
[ValidationResultBuilder](T_Tessa_Platform_Validation_ValidationResultBuilder.htm)|
Объект, выполняющий построение результата валидации.  
[ValidationResultItem](T_Tessa_Platform_Validation_ValidationResultItem.htm)|
Сообщение о валидации.  
[ValidationSequence](T_Tessa_Platform_Validation_ValidationSequence.htm)|
Отправная точка для процесса валидации.  
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm)|
Строго типизированный декоратор для хранилища IDictionary<string, object>,
поддерживающий валидацию свойств.  
[ValidationStorageResultBuilder](T_Tessa_Platform_Validation_ValidationStorageResultBuilder.htm)|
Объект, выполняющий построение результата валидации в хранилище
Dictionary<string, object>.  
[ValidationStorageResultItem](T_Tessa_Platform_Validation_ValidationStorageResultItem.htm)|
Сообщение о валидации, содержащееся в хранилище Dictionary<string, object>.  
[Validator](T_Tessa_Platform_Validation_Validator.htm)|  Объект,
осуществляющий валидацию свойств.  
## __Интерфейсы
[IValidatable](T_Tessa_Platform_Validation_IValidatable.htm)|  Объект,
поддерживающий базовую валидацию.  
---|---  
[IValidationKeyRegistry](T_Tessa_Platform_Validation_IValidationKeyRegistry.htm)|
Реестр ключей валидации
[ValidationKey](T_Tessa_Platform_Validation_ValidationKey.htm).  
[IValidationObject](T_Tessa_Platform_Validation_IValidationObject.htm)|
Объект, поддерживающий валидацию свойств.  
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)|
Объект, выполняющий построение результата валидации.  
[IValidationResultItem](T_Tessa_Platform_Validation_IValidationResultItem.htm)|
Сообщение о валидации.  
## __Перечисления
[ValidationLevel](T_Tessa_Platform_Validation_ValidationLevel.htm)|  Режим
вывода текста в результате валидации.  
---|---  
[ValidationResultType](T_Tessa_Platform_Validation_ValidationResultType.htm)|
Тип сообщения о валидации.
