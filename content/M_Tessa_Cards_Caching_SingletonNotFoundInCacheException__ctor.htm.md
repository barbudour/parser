# SingletonNotFoundInCacheException - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SingletonNotFoundInCacheException(
    	string cardTypeName,
    	ValidationResult validationResult
    )
VB __Копировать
     Public Sub New ( 
    	cardTypeName As String,
    	validationResult As ValidationResult
    )
C++ __Копировать
     public:
    SingletonNotFoundInCacheException(
    	String^ cardTypeName, 
    	ValidationResult^ validationResult
    )
F# __Копировать
     new : 
            cardTypeName : string * 
            validationResult : ValidationResult -> SingletonNotFoundInCacheException
#### Параметры
cardTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя типа карточки-синглтона, который не удалось загрузить.
validationResult
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)
     Результат неудачной валидации для процесса загрузки карточки-синглтона. 
## __См. также
#### Ссылки
[SingletonNotFoundInCacheException -
](T_Tessa_Cards_Caching_SingletonNotFoundInCacheException.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
