# CardGetRequest.TryGetAuthorTaskRowIDList - метод
Возвращает список идентификаторов заданий, все данные которых будут полностью
загружены, если такие задания доступны от имени автора, или null, если список
ещё не был задан.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IList<Guid> TryGetAuthorTaskRowIDList()
VB __Копировать
     Public Function TryGetAuthorTaskRowIDList As IList(Of Guid)
C++ __Копировать
     public:
    IList<Guid>^ TryGetAuthorTaskRowIDList()
F# __Копировать
     member TryGetAuthorTaskRowIDList : unit -> IList<Guid> 
#### Возвращаемое значение
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>  
Список идентификаторов заданий, все данные которых будут полностью загружены,
если такие задания доступны от имени автора, или null, если список ещё не был
задан.
## __См. также
#### Ссылки
[CardGetRequest - ](T_Tessa_Cards_CardGetRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
