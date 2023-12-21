# CardFileManager - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileManager(
    	CreateFileSourceForCardFuncAsync createFileSourceForCardFuncAsync,
    	CreateFileContainerFuncAsync createFileContainerFuncAsync,
    	StoreCardFuncAsync storeCardFuncAsync,
    	ISession session
    )
VB __Копировать
     Public Sub New ( 
    	createFileSourceForCardFuncAsync As CreateFileSourceForCardFuncAsync,
    	createFileContainerFuncAsync As CreateFileContainerFuncAsync,
    	storeCardFuncAsync As StoreCardFuncAsync,
    	session As ISession
    )
C++ __Копировать
     public:
    CardFileManager(
    	CreateFileSourceForCardFuncAsync^ createFileSourceForCardFuncAsync, 
    	CreateFileContainerFuncAsync^ createFileContainerFuncAsync, 
    	StoreCardFuncAsync^ storeCardFuncAsync, 
    	ISession^ session
    )
F# __Копировать
     new : 
            createFileSourceForCardFuncAsync : CreateFileSourceForCardFuncAsync * 
            createFileContainerFuncAsync : CreateFileContainerFuncAsync * 
            storeCardFuncAsync : StoreCardFuncAsync * 
            session : ISession -> CardFileManager
#### Параметры
createFileSourceForCardFuncAsync
[CreateFileSourceForCardFuncAsync](T_Tessa_Cards_CreateFileSourceForCardFuncAsync.htm)
    Функция, которая создаёт источник файлов для заданной карточки.
createFileContainerFuncAsync
[CreateFileContainerFuncAsync](T_Tessa_Files_CreateFileContainerFuncAsync.htm)
    Функция, которая создаёт контейнер файлов для заданного источника файлов.
storeCardFuncAsync [StoreCardFuncAsync](T_Tessa_Cards_StoreCardFuncAsync.htm)
    Функция, которая выполняет асинхронное сохранение карточки с файлами.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия текущего сотрудника.
##  __См. также
#### Ссылки
[CardFileManager - ](T_Tessa_Cards_CardFileManager.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
