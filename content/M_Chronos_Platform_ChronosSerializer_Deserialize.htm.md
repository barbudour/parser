# ChronosSerializer.Deserialize - метод
Десериализует текст в формате JSON.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public Dictionary<string, Object> Deserialize(
    	string text
    )
VB __Копировать
     Public Function Deserialize ( 
    	text As String
    ) As Dictionary(Of String, Object)
C++ __Копировать
     public:
    Dictionary<String^, Object^>^ Deserialize(
    	String^ text
    )
F# __Копировать
     member Deserialize : 
            text : string -> Dictionary<string, Object> 
#### Параметры
text [String](https://learn.microsoft.com/dotnet/api/system.string)
    Текст, который требуется десериализовать.
#### Возвращаемое значение
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>  
Десериализованный текст.
##  __См. также
#### Ссылки
[ChronosSerializer - ](T_Chronos_Platform_ChronosSerializer.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
