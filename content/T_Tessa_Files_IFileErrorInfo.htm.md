# IFileErrorInfo - интерфейс
Информация по ошибке, которая возникла при сохранении файла.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileErrorInfo : ICloneable
VB __Копировать
     Public Interface IFileErrorInfo
    	Inherits ICloneable
C++ __Копировать
     public interface class IFileErrorInfo : ICloneable
F# __Копировать
     type IFileErrorInfo = 
        interface
            interface ICloneable
        end
Implements
    [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable)
##  __Свойства
[DateTime](P_Tessa_Files_IFileErrorInfo_DateTime.htm)| Дата возникновения
ошибки.  
---|---  
[Message](P_Tessa_Files_IFileErrorInfo_Message.htm)| Текст сообщения об
ошибке.  
##  __Методы
[Clone](M_Tessa_Files_IFileErrorInfo_Clone.htm)| Создаёт полную копию объекта
с информацией по ошибке.  
---|---  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
