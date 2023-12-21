# ICardStreamGetStrategy - интерфейс
Стратегия, выполняющая потоковое получение контента файлов.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardStreamGetStrategy
VB __Копировать
     Public Interface ICardStreamGetStrategy
C++ __Копировать
     public interface class ICardStreamGetStrategy
F# __Копировать
     type ICardStreamGetStrategy = interface end
##  __Методы
[GetFileContentAsync](M_Tessa_Cards_ComponentModel_ICardStreamGetStrategy_GetFileContentAsync.htm)|
Получает контент версии файла. Возвращает ответ на запрос по получению
контента версии файла. Вторым параметром возвращает функцию, открывающую поток
на чтение контента файла, или null, если при получении информации о файле
возникла ошибка, причём отличное от null значение возвращается только в случае
отсутствия ошибок.  
---|---  
## __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
