# CardTaskDialogHelper.GetCompletionOptionSettings(IDictionary<String,
Object>, Guid) - метод
Возвращает параметры диалога имеющие указанный идентификатор.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardTaskCompletionOptionSettings? GetCompletionOptionSettings(
    	IDictionary<string, Object?>? settings,
    	Guid completionOptionID
    )
VB __Копировать
     Public Shared Function GetCompletionOptionSettings ( 
    	settings As IDictionary(Of String, Object),
    	completionOptionID As Guid
    ) As CardTaskCompletionOptionSettings
C++ __Копировать
     public:
    static CardTaskCompletionOptionSettings^ GetCompletionOptionSettings(
    	IDictionary<String^, Object^>^ settings, 
    	Guid completionOptionID
    )
F# __Копировать
     static member GetCompletionOptionSettings : 
            settings : IDictionary<string, Object> * 
            completionOptionID : Guid -> CardTaskCompletionOptionSettings 
#### Параметры
settings
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Коллекция ключ-значение содержащая параметры диалога.
completionOptionID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор варианта завершения.
#### Возвращаемое значение
[CardTaskCompletionOptionSettings](T_Tessa_Cards_CardTaskCompletionOptionSettings.htm)  
Параметры варианта завершения диалога или значение по умолчанию для типа, если
параметры не удалось получить.
##  __См. также
#### Ссылки
[CardTaskDialogHelper - ](T_Tessa_Cards_CardTaskDialogHelper.htm)
[GetCompletionOptionSettings -
перегрузка](Overload_Tessa_Cards_CardTaskDialogHelper_GetCompletionOptionSettings.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
