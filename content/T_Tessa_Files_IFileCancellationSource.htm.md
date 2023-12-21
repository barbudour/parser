# IFileCancellationSource - интерфейс
Объект, управляющий отменой асинхронных операций с файлами.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileCancellationSource : IDisposable
VB __Копировать
     Public Interface IFileCancellationSource
    	Inherits IDisposable
C++ __Копировать
     public interface class IFileCancellationSource : IDisposable
F# __Копировать
     type IFileCancellationSource = 
        interface
            interface IDisposable
        end
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Свойства
[IsCancellationRequested](P_Tessa_Files_IFileCancellationSource_IsCancellationRequested.htm)|
Признак того, что текущий объект запросил отмену связанных с ним асинхронных
операций.  
---|---  
[Token](P_Tessa_Files_IFileCancellationSource_Token.htm)| Токен, используемый
в асинхронных операциях, которые могут быть отменены.  
##  __Методы
[Cancel](M_Tessa_Files_IFileCancellationSource_Cancel.htm)| Отменяет все
асинхронные операции, связанные с текущим объектом.  
---|---  
[Dispose](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose)| Performs application-defined tasks associated with
freeing, releasing, or resetting unmanaged resources.  
(Унаследован от
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable))  
[Reset](M_Tessa_Files_IFileCancellationSource_Reset.htm)|  Восстанавливает
возможность выполнения для асинхронных операций, которые будут связаны с
текущим объектом. Если отмена ещё не выполнялась или ни одной связанной
асинхронной операции не создано, то метод не выполняет действий.  
## __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
