# CardCacheValue<T>.Success - метод
Создаёт объект со значением, для которого считается, что это значение было
успешно получено из кэша. Свойство
[Result](P_Tessa_Cards_Caching_CardCacheValue_1_Result.htm) созданного объекта
равно [Success](T_Tessa_Cards_Caching_CardCacheResult.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardCacheValue<T> Success(
    	string key,
    	T value,
    	ValidationResult validationResult = null
    )
VB __Копировать
     Public Shared Function Success ( 
    	key As String,
    	value As T,
    	Optional validationResult As ValidationResult = Nothing
    ) As CardCacheValue(Of T)
C++ __Копировать
     public:
    static CardCacheValue<T> Success(
    	String^ key, 
    	T value, 
    	ValidationResult^ validationResult = nullptr
    )
F# __Копировать
     static member Success : 
            key : string * 
            value : 'T * 
            ?validationResult : ValidationResult 
    (* Defaults:
            let _validationResult = defaultArg validationResult null
    *)
    -> CardCacheValue<'T> 
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, по которому было запрошено значение.
value [T](T_Tessa_Cards_Caching_CardCacheValue_1.htm)
    Полученное значение.
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
