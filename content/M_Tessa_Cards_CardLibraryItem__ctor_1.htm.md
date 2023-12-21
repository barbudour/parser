# CardLibraryItem(String, String) - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardLibraryItem(
    	string path,
    	string description = null
    )
VB __Копировать
     Public Sub New ( 
    	path As String,
    	Optional description As String = Nothing
    )
C++ __Копировать
     public:
    CardLibraryItem(
    	String^ path, 
    	String^ description = nullptr
    )
F# __Копировать
     new : 
            path : string * 
            ?description : string 
    (* Defaults:
            let _description = defaultArg description null
    *)
    -> CardLibraryItem
#### Параметры
path [String](https://learn.microsoft.com/dotnet/api/system.string)
    Относительный путь от файла библиотеки до файла с карточкой.
description [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
    Описание карточки.
##  __См. также
#### Ссылки
[CardLibraryItem - ](T_Tessa_Cards_CardLibraryItem.htm)
[CardLibraryItem - перегрузка](Overload_Tessa_Cards_CardLibraryItem__ctor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
