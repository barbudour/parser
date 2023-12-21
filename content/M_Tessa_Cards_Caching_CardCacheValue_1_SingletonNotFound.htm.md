# CardCacheValue<T>.SingletonNotFound - метод
Создаёт объект, который содержит ошибку: карточка-синглтон (такая как карточка
настроек) не найдена в кэше по ключу key. Свойство
[Result](P_Tessa_Cards_Caching_CardCacheValue_1_Result.htm) созданного объекта
равно [SingletonNotFound](T_Tessa_Cards_Caching_CardCacheResult.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardCacheValue<T> SingletonNotFound(
    	string key,
    	ValidationResult validationResult = null
    )
VB __Копировать
     Public Shared Function SingletonNotFound ( 
    	key As String,
    	Optional validationResult As ValidationResult = Nothing
    ) As CardCacheValue(Of T)
C++ __Копировать
     public:
    static CardCacheValue<T> SingletonNotFound(
    	String^ key, 
    	ValidationResult^ validationResult = nullptr
    )
F# __Копировать
     static member SingletonNotFound : 
            key : string * 
            ?validationResult : ValidationResult 
    (* Defaults:
            let _validationResult = defaultArg validationResult null
    *)
    -> CardCacheValue<'T> 
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, по которому было запрошено значение.
validationResult
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)
(Optional)
    Сообщения валидации или null, если сообщения валидации отсутствуют.
#### Возвращаемое значение
[CardCacheValue](T_Tessa_Cards_Caching_CardCacheValue_1.htm)<[T](T_Tessa_Cards_Caching_CardCacheValue_1.htm)>  
Созданное значение.
##  __См. также
#### Ссылки
[CardCacheValue<T> \- ](T_Tessa_Cards_Caching_CardCacheValue_1.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
