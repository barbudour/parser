# FileSourceForCardContext(Boolean, FileSourceForCardContextExecutorAsync) -
конструктор
Создаёт экземпляр класса с указанием значений его свойств и методов.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileSourceForCardContext(
    	bool enableSignatures,
    	FileSourceForCardContextExecutorAsync contextExecutorAsync
    )
VB __Копировать
     Public Sub New ( 
    	enableSignatures As Boolean,
    	contextExecutorAsync As FileSourceForCardContextExecutorAsync
    )
C++ __Копировать
     public:
    FileSourceForCardContext(
    	bool enableSignatures, 
    	FileSourceForCardContextExecutorAsync^ contextExecutorAsync
    )
F# __Копировать
     new : 
            enableSignatures : bool * 
            contextExecutorAsync : FileSourceForCardContextExecutorAsync -> FileSourceForCardContext
#### Параметры
enableSignatures
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак того, что для источника файлов разрешена загрузка подписей от сервиса карточек. 
contextExecutorAsync
[FileSourceForCardContextExecutorAsync](T_Tessa_Cards_FileSourceForCardContextExecutorAsync.htm)
     Действие в контексте карточки с указанием имени карточки или null, если действие выполняется без дополнительного контекста. 
## __См. также
#### Ссылки
[FileSourceForCardContext - ](T_Tessa_Cards_FileSourceForCardContext.htm)
[FileSourceForCardContext -
перегрузка](Overload_Tessa_Cards_FileSourceForCardContext__ctor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
