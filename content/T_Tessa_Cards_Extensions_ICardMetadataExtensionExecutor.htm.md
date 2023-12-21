# ICardMetadataExtensionExecutor - интерфейс
Объект, обеспечивающий выполнение расширений для метаинформации по типам
карточек
[ICardMetadataExtension](T_Tessa_Cards_Extensions_ICardMetadataExtension.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardMetadataExtensionExecutor : IAsyncDisposable
VB __Копировать
     Public Interface ICardMetadataExtensionExecutor
    	Inherits IAsyncDisposable
C++ __Копировать
     public interface class ICardMetadataExtensionExecutor : IAsyncDisposable
F# __Копировать
     type ICardMetadataExtensionExecutor = 
        interface
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
##  __Заметки
После завершения работы с объектом следует вызвать метод
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose), чтобы освободить экземпляры расширений.
## __Методы
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
---|---  
[ModifyMetadataAsync](M_Tessa_Cards_Extensions_ICardMetadataExtensionExecutor_ModifyMetadataAsync.htm)|
Выполняет расширения, изменяющие метаинформацию по типам карточек после её
построения.  
[ModifyTypesAsync](M_Tessa_Cards_Extensions_ICardMetadataExtensionExecutor_ModifyTypesAsync.htm)|
Выполняет расширения, изменяющие типы карточек, по которым затем будет
строиться метаинформация.  
##  __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
