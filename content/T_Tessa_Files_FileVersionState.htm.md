# FileVersionState - перечисление
Состояние версии файла.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum FileVersionState
VB __Копировать
     Public Enumeration FileVersionState
C++ __Копировать
     public enum class FileVersionState
F# __Копировать
     type FileVersionState
##  __Члены
Created| 0|  Версия создана локально, её загрузка во внешнюю подсистему ещё не
начиналась.  
---|---|---  
Uploading| 1|  Версия файла в процессе загрузки во внешнюю подсистему.  
Success| 2|  Версия файла успешно загружена во внешнюю подсистему.  
Error| 3|  Версия файла загружена во внешнюю подсистему с ошибкой.  
## __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
