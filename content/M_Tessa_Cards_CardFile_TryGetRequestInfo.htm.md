# CardFile.TryGetRequestInfo - метод
Возвращает дополнительную пользовательскую информацию по текущему объекту,
передаваемую в запросы
[CardGetFileContentRequest](T_Tessa_Cards_CardGetFileContentRequest.htm) и
[CardGetFileVersionsRequest](T_Tessa_Cards_CardGetFileVersionsRequest.htm), и
в запрос на загрузку списка подписей
[GetVersionSignatures](F_Tessa_Cards_CardRequestTypes_GetVersionSignatures.htm),
или null, если информация ещё не была задана.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Dictionary<string, Object> TryGetRequestInfo()
VB __Копировать
     Public Function TryGetRequestInfo As Dictionary(Of String, Object)
C++ __Копировать
     public:
    Dictionary<String^, Object^>^ TryGetRequestInfo()
F# __Копировать
     member TryGetRequestInfo : unit -> Dictionary<string, Object> 
#### Возвращаемое значение
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>  
Дополнительная пользовательская информация по текущему объекту, передаваемая в
запросы
[CardGetFileContentRequest](T_Tessa_Cards_CardGetFileContentRequest.htm) и
[CardGetFileVersionsRequest](T_Tessa_Cards_CardGetFileVersionsRequest.htm), и
в запрос на загрузку списка подписей
[GetVersionSignatures](F_Tessa_Cards_CardRequestTypes_GetVersionSignatures.htm),
или null, если информация ещё не была задана.
## __См. также
#### Ссылки
[CardFile - ](T_Tessa_Cards_CardFile.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
