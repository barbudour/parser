# FileContentDownloadState - перечисление
Состояние загрузки в кэш для контента версии файла для последующего
отображения пользователю.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum FileContentDownloadState
VB __Копировать
     Public Enumeration FileContentDownloadState
C++ __Копировать
     public enum class FileContentDownloadState
F# __Копировать
     type FileContentDownloadState
##  __Члены
None| 0|  Контент отсутствует в кэше, т.е. ещё не был загружен или был
загружен с ошибкой.  
---|---|---  
InProgress| 1|  Загрузка контента в процессе выполнения. Не рекомендуется
параллельно запускать ещё один процесс, загружающий контент. Желательно
дождаться смены состояния.  
Success| 2|  Контент успешно загружен и доступен для отображения пользователю.  
Error| 3|  Контент загружен с ошибкой и недоступен для отображения
пользователю.  
## __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
