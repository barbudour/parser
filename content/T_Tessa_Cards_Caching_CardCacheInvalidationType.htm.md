# CardCacheInvalidationType - перечисление
Тип операции по сбросу кэша.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum CardCacheInvalidationType
VB __Копировать
     Public Enumeration CardCacheInvalidationType
C++ __Копировать
     public enum class CardCacheInvalidationType
F# __Копировать
     type CardCacheInvalidationType
##  __Члены
Everything| 0|  Вызывается полный сброс кэша карточек и настроек.  
---|---|---  
Cards| 1|  Вызывается полный сброс кэша карточек или сброс для карточки с
заданным ключом, если ключ отличен от null.  
Settings| 2|  Вызывается полный сброс кэша настроек или сброс для настройки с
заданным ключом, если ключ отличен от null.  
## __См. также
#### Ссылки
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
