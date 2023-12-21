# IDocLoadDocument - интерфейс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.DocLoad](N_Tessa_Extensions_Platform_Server_DocLoad.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IDocLoadDocument : IAsyncDisposable
VB __Копировать
     Public Interface IDocLoadDocument
    	Inherits IAsyncDisposable
C++ __Копировать
     public interface class IDocLoadDocument : IAsyncDisposable
F# __Копировать
     type IDocLoadDocument = 
        interface
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
##  __Свойства
[Barcode](P_Tessa_Extensions_Platform_Server_DocLoad_IDocLoadDocument_Barcode.htm)|
Штрих-код документа  
---|---  
[CardID](P_Tessa_Extensions_Platform_Server_DocLoad_IDocLoadDocument_CardID.htm)|
ID карточки  
[File](P_Tessa_Extensions_Platform_Server_DocLoad_IDocLoadDocument_File.htm)|
Имя файла документа  
[InputFilePath](P_Tessa_Extensions_Platform_Server_DocLoad_IDocLoadDocument_InputFilePath.htm)|
Имя файла документа  
[PageCount](P_Tessa_Extensions_Platform_Server_DocLoad_IDocLoadDocument_PageCount.htm)|
Количество страниц в документе  
## __Методы
[AppendPageAsync](M_Tessa_Extensions_Platform_Server_DocLoad_IDocLoadDocument_AppendPageAsync.htm)|
Добавить страницу к документу  
---|---  
[CloseAsync](M_Tessa_Extensions_Platform_Server_DocLoad_IDocLoadDocument_CloseAsync.htm)|
Закрывает обработку  
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
[GetExtension](M_Tessa_Extensions_Platform_Server_DocLoad_IDocLoadDocument_GetExtension.htm)|
Возвращает расширение файла для сохранения  
## __См. также
#### Ссылки
[Tessa.Extensions.Platform.Server.DocLoad - пространство
имён](N_Tessa_Extensions_Platform_Server_DocLoad.htm)
