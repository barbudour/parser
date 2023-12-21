# IFileContentNameReplacer - интерфейс
Объект, выполняющий исправление имени файла, создаваемого в кэше. Например,
имя файла может сокращаться, из него могут исключаться некорректные символы.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileContentNameReplacer
VB __Копировать
     Public Interface IFileContentNameReplacer
C++ __Копировать
     public interface class IFileContentNameReplacer
F# __Копировать
     type IFileContentNameReplacer = interface end
##  __Методы
[CoerceName](M_Tessa_Files_IFileContentNameReplacer_CoerceName.htm)|
Исправляет имя файла (без пути к файлу), которое будет использоваться для
сохранения содержимого файла в кэше (во временной папке).  
---|---  
## __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
