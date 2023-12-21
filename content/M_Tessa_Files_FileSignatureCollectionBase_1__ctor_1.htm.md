# FileSignatureCollectionBase<TCollection>(IEnumerable<IFileSignature>) -
конструктор
Создаёт экземпляр коллекции, в которую копируются элементы из заданной
коллекции. Не выполняет клонирование переданных элементов.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected FileSignatureCollectionBase(
    	IEnumerable<IFileSignature> collection
    )
VB __Копировать
     Protected Sub New ( 
    	collection As IEnumerable(Of IFileSignature)
    )
C++ __Копировать
     protected:
    FileSignatureCollectionBase(
    	IEnumerable<IFileSignature^>^ collection
    )
F# __Копировать
     new : 
            collection : IEnumerable<IFileSignature> -> FileSignatureCollectionBase
#### Параметры
collection
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>
    Коллекция, элементы которой копируются в создаваемую коллекцию.
##  __См. также
#### Ссылки
[FileSignatureCollectionBase<TCollection> \-
](T_Tessa_Files_FileSignatureCollectionBase_1.htm)
[FileSignatureCollectionBase<TCollection> \-
перегрузка](Overload_Tessa_Files_FileSignatureCollectionBase_1__ctor.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
