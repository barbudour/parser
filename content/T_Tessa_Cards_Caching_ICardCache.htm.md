# ICardCache - интерфейс
Потокобезопасный кэш с карточками и дополнительными настройками.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardCache
VB __Копировать
     Public Interface ICardCache
C++ __Копировать
     public interface class ICardCache
F# __Копировать
     type ICardCache = interface end
##  __Свойства
[Cards](P_Tessa_Cards_Caching_ICardCache_Cards.htm)| Кэш карточек, доступных
по строковому ключу.  
---|---  
[Settings](P_Tessa_Cards_Caching_ICardCache_Settings.htm)| Кэш настроек,
доступных по строковому ключу и функции заполнения значения, отсутствующего в
кэше.  
##  __Методы
[InvalidateAsync](M_Tessa_Cards_Caching_ICardCache_InvalidateAsync.htm)|
Сбрасывает локальный кэш.  
---|---  
##  __См. также
#### Ссылки
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
