# CardCacheValue<T> \- свойства
##  __Свойства
[IsSuccess](P_Tessa_Cards_Caching_CardCacheValue_1_IsSuccess.htm)|  Признак
того, что значение может быть успешно получено через метод
[GetValue()](M_Tessa_Cards_Caching_CardCacheValue_1_GetValue.htm). Аналогично
проверке того, что свойство
[Result](P_Tessa_Cards_Caching_CardCacheValue_1_Result.htm) равно
[Success](T_Tessa_Cards_Caching_CardCacheResult.htm).  
---|---  
[Key](P_Tessa_Cards_Caching_CardCacheValue_1_Key.htm)|  Ключ, по которому было
запрошено значение из кэша.  
[Result](P_Tessa_Cards_Caching_CardCacheValue_1_Result.htm)|  Результат
обращения к кэшу. Если возвращено значение
[Success](T_Tessa_Cards_Caching_CardCacheResult.htm), то можно вызвать метод
[GetValue()](M_Tessa_Cards_Caching_CardCacheValue_1_GetValue.htm), который
вернёт значение без выбрасывания исключений.  
[ValidationResult](P_Tessa_Cards_Caching_CardCacheValue_1_ValidationResult.htm)|
Сообщения валидации. Могут содержать ошибки и предупреждения, возникшие в
процессе получения значения из кэша, например, в процессе загрузки карточки
настроек, если это кэш карточек-синглтонов. Не равен null.  
## __См. также
#### Ссылки
[CardCacheValue<T> \- ](T_Tessa_Cards_Caching_CardCacheValue_1.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
