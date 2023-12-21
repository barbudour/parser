# EmptyFileSource - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public EmptyFileSource(
    	IFileCache cache,
    	ISession session
    )
VB __Копировать
     Public Sub New ( 
    	cache As IFileCache,
    	session As ISession
    )
C++ __Копировать
     public:
    EmptyFileSource(
    	IFileCache^ cache, 
    	ISession^ session
    )
F# __Копировать
     new : 
            cache : IFileCache * 
            session : ISession -> EmptyFileSource
#### Параметры
cache [IFileCache](T_Tessa_Files_IFileCache.htm)
    Кэш для контента файлов.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
     Сессия пользователя, который используется для автоматического заполнения свойств в создаваемых токенах для файлов и версий файлов. 
## __См. также
#### Ссылки
[EmptyFileSource - ](T_Tessa_Files_EmptyFileSource.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
