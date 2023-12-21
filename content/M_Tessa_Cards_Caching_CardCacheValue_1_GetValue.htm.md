# CardCacheValue<T>.GetValue - метод
Возвращает значение, полученное из кэша. Выбрасывает исключение, если
результат обращения к кэшу
[Result](P_Tessa_Cards_Caching_CardCacheValue_1_Result.htm) отличен от
успешного [Success](T_Tessa_Cards_Caching_CardCacheResult.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public T GetValue()
VB __Копировать
     Public Function GetValue As T
C++ __Копировать
     public:
    T GetValue()
F# __Копировать
     member GetValue : unit -> 'T 
#### Возвращаемое значение
[T](T_Tessa_Cards_Caching_CardCacheValue_1.htm)  
Значение, полученное из кэша.
##  __Исключения
[ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception)|
Переданный ключ [Key](P_Tessa_Cards_Caching_CardCacheValue_1_Key.htm) является
недопустимым для кэша. Соответствует результату
[InvalidKey](T_Tessa_Cards_Caching_CardCacheResult.htm).  
---|---  
[ArgumentOutOfRangeException](https://learn.microsoft.com/dotnet/api/system.argumentoutofrangeexception)|
Неизвестное значение перечисления
[CardCacheResult](T_Tessa_Cards_Caching_CardCacheResult.htm) в свойстве
[Result](P_Tessa_Cards_Caching_CardCacheValue_1_Result.htm).  
[SingletonNotFoundInCacheException](T_Tessa_Cards_Caching_SingletonNotFoundInCacheException.htm)|
Карточка-синглтон (такая как карточка настроек) не найдена в кэше.
Соответствует результату
[SingletonNotFound](T_Tessa_Cards_Caching_CardCacheResult.htm).  
## __См. также
#### Ссылки
[CardCacheValue<T> \- ](T_Tessa_Cards_Caching_CardCacheValue_1.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
