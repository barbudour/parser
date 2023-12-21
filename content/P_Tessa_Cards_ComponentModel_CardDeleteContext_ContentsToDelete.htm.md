# CardDeleteContext.ContentsToDelete - свойство
Список контентов файлов, для которых было выполнено или должно быть выполнено
удаление, в зависимости от признака
[KeepFileContent](P_Tessa_Cards_ComponentModel_CardDeleteContext_KeepFileContent.htm).
Может быть равен null, если файлы отсутствуют и не требуется выполнять
действий.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public List<CardContentContext> ContentsToDelete { get; set; }
VB __Копировать
     Public Property ContentsToDelete As List(Of CardContentContext)
    	Get
    	Set
C++ __Копировать
     public:
    property List<CardContentContext^>^ ContentsToDelete {
    	List<CardContentContext^>^ get ();
    	void set (List<CardContentContext^>^ value);
    }
F# __Копировать
     member ContentsToDelete : List<CardContentContext> with get, set
#### Значение свойства
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[CardContentContext](T_Tessa_Cards_ComponentModel_CardContentContext.htm)>
##  __См. также
#### Ссылки
[CardDeleteContext - ](T_Tessa_Cards_ComponentModel_CardDeleteContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
