# CardFileContentProvider(Guid, Byte[]) - конструктор
Создаёт экземпляр класса для файлов, контент которых задаётся в виде массива
байт.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileContentProvider(
    	Guid fileID,
    	byte[] content
    )
VB __Копировать
     Public Sub New ( 
    	fileID As Guid,
    	content As Byte()
    )
C++ __Копировать
     public:
    CardFileContentProvider(
    	Guid fileID, 
    	array<unsigned char>^ content
    )
F# __Копировать
     new : 
            fileID : Guid * 
            content : byte[] -> CardFileContentProvider
#### Параметры
fileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор файла.
content [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
    Контент файла, не может быть равен null.
##  __См. также
#### Ссылки
[CardFileContentProvider - ](T_Tessa_Cards_CardFileContentProvider.htm)
[CardFileContentProvider -
перегрузка](Overload_Tessa_Cards_CardFileContentProvider__ctor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
