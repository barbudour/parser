# FileCategory - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileCategory(
    	Guid? id,
    	string caption
    )
VB __Копировать
     Public Sub New ( 
    	id As Guid?,
    	caption As String
    )
C++ __Копировать
     public:
    FileCategory(
    	Nullable<Guid> id, 
    	String^ caption
    )
F# __Копировать
     new : 
            id : Nullable<Guid> * 
            caption : string -> FileCategory
#### Параметры
id
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Уникальный идентификатор категории файла или null, если категория не имеет идентификатора. 
caption [String](https://learn.microsoft.com/dotnet/api/system.string)
    Отображаемое имя категории файла, которое видит пользователь.
##  __См. также
#### Ссылки
[FileCategory - ](T_Tessa_Files_FileCategory.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
