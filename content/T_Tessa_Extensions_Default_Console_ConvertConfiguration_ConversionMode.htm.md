# ConversionMode - перечисление
Режим преобразования конфигурации.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Console.ConvertConfiguration](N_Tessa_Extensions_Default_Console_ConvertConfiguration.htm)  
 **Сборка:** Tessa.Extensions.Default.Console (в
Tessa.Extensions.Default.Console.dll) Версия: 3.6.0.17
C# __Копировать
     public enum ConversionMode
VB __Копировать
     Public Enumeration ConversionMode
C++ __Копировать
     public enum class ConversionMode
F# __Копировать
     type ConversionMode
##  __Члены
Upgrade| 0|  Преобразовать объекты конфигурации до форматов в текущей версии
платформы.  
---|---|---  
Downgrade| 1|  Преобразовать файлы конфигурации в старые форматы, совместимые
с предыдущими версиями платформы.  
LF| 2|  Переводы строк преобразуются в символ LF, которые совместимы с Windows
и Linux. Это рекомендуемый формат.  
CRLF| 3|  Переводы строк преобразуются в символы CR LF, которые совместимы с
Windows. Используйте для сравнения с объектами, выгруженными в предыдущих
версиях платформы из приложений TessaAdmin или посредством команды tadmin на
Windows.  
BOM| 4|  Кодировка файлов преобразутеся из UTF-8 в UTF-8 с BOM.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Console.ConvertConfiguration - пространство
имён](N_Tessa_Extensions_Default_Console_ConvertConfiguration.htm)
