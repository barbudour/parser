# CardFileVersion.RequestInfo - свойство
Дополнительная пользовательская информация, передаваемая в запрос
[CardGetFileContentRequest](T_Tessa_Cards_CardGetFileContentRequest.htm) и в
запрос на загрузку списка подписей
[GetVersionSignatures](F_Tessa_Cards_CardRequestTypes_GetVersionSignatures.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Dictionary<string, Object> RequestInfo { get; set; }
VB __Копировать
     Public Property RequestInfo As Dictionary(Of String, Object)
    	Get
    	Set
C++ __Копировать
     public:
    property Dictionary<String^, Object^>^ RequestInfo {
    	Dictionary<String^, Object^>^ get ();
    	void set (Dictionary<String^, Object^>^ value);
    }
F# __Копировать
     member RequestInfo : Dictionary<string, Object> with get, set
#### Значение свойства
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
##  __См. также
#### Ссылки
[CardFileVersion - ](T_Tessa_Cards_CardFileVersion.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
