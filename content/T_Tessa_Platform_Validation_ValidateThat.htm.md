# ValidateThat - класс
Предикаты для процесса валидации.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Validation](N_Tessa_Platform_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ValidateThat
VB __Копировать
     Public NotInheritable Class ValidateThat
C++ __Копировать
     public ref class ValidateThat abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ValidateThat = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ValidateThat
##  __Методы
[DateTimeIsNotEmpty](M_Tessa_Platform_Validation_ValidateThat_DateTimeIsNotEmpty.htm)|
Метод валидации, проверяющий, что переданная дата не является
DateTime.MinValue.  
---|---  
[EverythingIsValid<T>(IEnumerable<T>)](M_Tessa_Platform_Validation_ValidateThat_EverythingIsValid__1.htm)|
Метод валидации, возвращающий признак того, что все заданные объекты прошли
валидацию.  
[EverythingIsValid<TKey, TValue>(IDictionary<TKey,
TValue>)](M_Tessa_Platform_Validation_ValidateThat_EverythingIsValid__2.htm)|
Метод валидации, возвращающий признак того, что все значения заданной
коллекции ключ / значение прошли валидацию.  
[FileNameIsValid](M_Tessa_Platform_Validation_ValidateThat_FileNameIsValid.htm)|
Метод валидации, проверяющий, что переданная строка является корректным именем
файла.  
[GuidIsNotEmpty](M_Tessa_Platform_Validation_ValidateThat_GuidIsNotEmpty.htm)|
Метод валидации, проверяющий, что переданный идентификатор
[Guid](https://learn.microsoft.com/dotnet/api/system.guid) не равен
Guid.Empty.  
[GuidIsNullOrNotEmpty](M_Tessa_Platform_Validation_ValidateThat_GuidIsNullOrNotEmpty.htm)|
Метод валидации, проверяющий, что переданный идентификатор
[Guid](https://learn.microsoft.com/dotnet/api/system.guid) не равен
Guid.Empty, при этом он может быть равен null.  
[Int32IsNullOrPositiveOrZero](M_Tessa_Platform_Validation_ValidateThat_Int32IsNullOrPositiveOrZero.htm)|
Метод валидации, проверяющий, что переданное число равно null или больше либо
равно нулю.  
[Int32IsPositive](M_Tessa_Platform_Validation_ValidateThat_Int32IsPositive.htm)|
Метод валидации, проверяющий, что переданное число больше нуля.  
[Int32IsPositiveOrZero](M_Tessa_Platform_Validation_ValidateThat_Int32IsPositiveOrZero.htm)|
Метод валидации, проверяющий, что переданное число больше либо равно нулю.  
[Int64IsNullOrPositiveOrZero](M_Tessa_Platform_Validation_ValidateThat_Int64IsNullOrPositiveOrZero.htm)|
Метод валидации, проверяющий, что переданное число равно null или больше либо
равно нулю.  
[Int64IsPositive](M_Tessa_Platform_Validation_ValidateThat_Int64IsPositive.htm)|
Метод валидации, проверяющий, что переданное число больше нуля.  
[Int64IsPositiveOrZero](M_Tessa_Platform_Validation_ValidateThat_Int64IsPositiveOrZero.htm)|
Метод валидации, проверяющий, что переданное число больше либо равно нулю.  
[ObjectIsNotNull](M_Tessa_Platform_Validation_ValidateThat_ObjectIsNotNull.htm)|
Метод валидации, проверяющий, что переданный объект не равен null.  
[ObjectIsValid<T>](M_Tessa_Platform_Validation_ValidateThat_ObjectIsValid__1.htm)|
Метод валидации, возвращающий признак того, что заданный объект прошёл
валидацию.  
[SingleIsNullOrPositiveOrZero](M_Tessa_Platform_Validation_ValidateThat_SingleIsNullOrPositiveOrZero.htm)|
Метод валидации, проверяющий, что переданное число равно null или больше либо
равно нулю.  
[SingleIsPositiveOrZero](M_Tessa_Platform_Validation_ValidateThat_SingleIsPositiveOrZero.htm)|
Метод валидации, проверяющий, что переданное число больше либо равно нулю.  
[StringIsNotNullOrEmpty](M_Tessa_Platform_Validation_ValidateThat_StringIsNotNullOrEmpty.htm)|
Метод валидации, проверяющий, что переданная строка не является пустой.  
[StringIsNotNullOrWhiteSpace](M_Tessa_Platform_Validation_ValidateThat_StringIsNotNullOrWhiteSpace.htm)|
Метод валидации, проверяющий, что переданная строка содержит символы, не
являющиеся пробелами.  
[ValueIsDefined<TEnum>](M_Tessa_Platform_Validation_ValidateThat_ValueIsDefined__1.htm)|
Метод валидации, проверяющий, что переданный объект определён как значение
перечисления в типе TEnum.  
## __См. также
#### Ссылки
[Tessa.Platform.Validation - пространство
имён](N_Tessa_Platform_Validation.htm)
