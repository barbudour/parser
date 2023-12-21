# FileResolverContext - конструктор
Создаёт экземпляр класса с указанием его параметров.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileResolverContext(
    	params Tuple<IFileSource, IFileSource>[] sourceItems
    )
VB __Копировать
     Public Sub New ( 
    	ParamArray sourceItems As Tuple(Of IFileSource, IFileSource)()
    )
C++ __Копировать
     public:
    FileResolverContext(
    	... array<Tuple<IFileSource^, IFileSource^>^>^ sourceItems
    )
F# __Копировать
     new : 
            sourceItems : Tuple<IFileSource, IFileSource>[] -> FileResolverContext
#### Параметры
sourceItems
[Tuple](https://learn.microsoft.com/dotnet/api/system.tuple-2)<[IFileSource](T_Tessa_Files_IFileSource.htm),
[IFileSource](T_Tessa_Files_IFileSource.htm)>[]
     Список кортежей, где первый элемент Item1 \- заменяемый источник файлов [IFileSource](T_Tessa_Files_IFileSource.htm), а второй элемент Item2 \- заменённый источник файлов. 
## __См. также
#### Ссылки
[FileResolverContext - ](T_Tessa_Files_FileResolverContext.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
