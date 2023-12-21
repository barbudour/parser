# ICardFileContainer - интерфейс
Контейнер, содержащий информацию по карточке и её файлам.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardFileContainer : IAsyncDisposable
VB __Копировать
     Public Interface ICardFileContainer
    	Inherits IAsyncDisposable
C++ __Копировать
     public interface class ICardFileContainer : IAsyncDisposable
F# __Копировать
     type ICardFileContainer = 
        interface
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
##  __Свойства
[Card](P_Tessa_Cards_ICardFileContainer_Card.htm)| Карточка.  
---|---  
[CreationResult](P_Tessa_Cards_ICardFileContainer_CreationResult.htm)|
Результат создания текущего объекта. Может содержать ошибки, связанные с
получением файлов.  
[FileContainer](P_Tessa_Cards_ICardFileContainer_FileContainer.htm)| Файлы,
относящиеся к карточке.  
[Manager](P_Tessa_Cards_ICardFileContainer_Manager.htm)| Объект, который
создал текущий контейнер.  
##  __Методы
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
---|---  
##  __Методы расширения
[StoreAsync](M_Tessa_Cards_CardExtensions_StoreAsync.htm)|  Сохраняет карточку
из текущего контейнера и контент её файлов, при этом позволяет асинхронно
отслеживать её состояние. В процессе сохранения карточка в контейнере и её
файлы не изменяются, поэтому метод безопасно вызывать повторно.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
