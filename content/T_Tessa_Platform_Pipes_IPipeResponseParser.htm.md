# IPipeResponseParser - интерфейс
Объект, выполняющий десериализацию объекта ответа на запрос из текста.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeResponseParser
VB __Копировать
     Public Interface IPipeResponseParser
C++ __Копировать
     public interface class IPipeResponseParser
F# __Копировать
     type IPipeResponseParser = interface end
##  __Методы
[TryParse](M_Tessa_Platform_Pipes_IPipeResponseParser_TryParse.htm)|
Десериализует из заданного текста объект ответа на запрос. Возвращает null,
если текст не содержит подходящего объекта. Тип объекта может отличаться в
зависимости от того, какие данные были сериализованы.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
