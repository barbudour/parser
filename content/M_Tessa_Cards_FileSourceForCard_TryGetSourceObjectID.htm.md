# FileSourceForCard.TryGetSourceObjectID - метод
Получает идентификатор объекта-хранилища для указанного файла.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override Guid? TryGetSourceObjectID(
    	IFile file
    )
VB __Копировать
     Public Overrides Function TryGetSourceObjectID ( 
    	file As IFile
    ) As Guid?
C++ __Копировать
     public:
    virtual Nullable<Guid> TryGetSourceObjectID(
    	IFile^ file
    ) override
F# __Копировать
     abstract TryGetSourceObjectID : 
            file : IFile -> Nullable<Guid> 
    override TryGetSourceObjectID : 
            file : IFile -> Nullable<Guid> 
#### Параметры
file [IFile](T_Tessa_Files_IFile.htm)
    Файл, для которого требуется получить идентификатор объекта-хранилища.
#### Возвращаемое значение
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>  
Идентификатор объекта или null, если объект не найден.
#### Реализации
[IFileSource.TryGetSourceObjectID(IFile)](M_Tessa_Files_IFileSource_TryGetSourceObjectID.htm)  
##  __См. также
#### Ссылки
[FileSourceForCard - ](T_Tessa_Cards_FileSourceForCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
