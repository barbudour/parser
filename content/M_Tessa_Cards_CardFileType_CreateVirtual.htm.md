# CardFileType.CreateVirtual - метод
Создаёт виртуальный тип файла, который по идентификатору и отображаемому имени
не отличается от стандартного типа
[FileTypeID](F_Tessa_Cards_CardHelper_FileTypeID.htm), но отличается по
уникальному имени [Name](P_Tessa_Cards_CardFileType_Name.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardFileType CreateVirtual(
    	string name
    )
VB __Копировать
     Public Shared Function CreateVirtual ( 
    	name As String
    ) As CardFileType
C++ __Копировать
     public:
    static CardFileType^ CreateVirtual(
    	String^ name
    )
F# __Копировать
     static member CreateVirtual : 
            name : string -> CardFileType 
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Уникальное имя типа файла в карточке.
#### Возвращаемое значение
[CardFileType](T_Tessa_Cards_CardFileType.htm)  
Созданный тип файла.
##  __См. также
#### Ссылки
[CardFileType - ](T_Tessa_Cards_CardFileType.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
