# CardCacheResult - перечисление
Результат обращения к кэшу с объектами API карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum CardCacheResult
VB __Копировать
     Public Enumeration CardCacheResult
C++ __Копировать
     public enum class CardCacheResult
F# __Копировать
     type CardCacheResult
##  __Члены
Unknown| 0|  Объект
[CardCacheValue<T>](T_Tessa_Cards_Caching_CardCacheValue_1.htm) был создан
конструктором по умолчанию, поэтому значение не заполнено.  
---|---|---  
Success| 1|  Значение успешно получено из кэша и доступно в методе
[GetValue()](M_Tessa_Cards_Caching_CardCacheValue_1_GetValue.htm)  
InvalidKey| 2|  Переданный ключ
[Key](P_Tessa_Cards_Caching_CardCacheValue_1_Key.htm) является недопустимым
для кэша.  
SingletonNotFound| 3|  Карточка-синглтон (такая как карточка настроек) не
найдена в кэше по ключу [Key](P_Tessa_Cards_Caching_CardCacheValue_1_Key.htm),
т.к. при её загрузке возникли ошибки, которые записаны в объекте
[ValidationResult](P_Tessa_Cards_Caching_CardCacheValue_1_ValidationResult.htm).
который  
## __См. также
#### Ссылки
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
