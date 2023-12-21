# CardPermissionFlagValues - класс
Константы для флагового перечисления
[CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CardPermissionFlagValues
VB __Копировать
     Public NotInheritable Class CardPermissionFlagValues
C++ __Копировать
     public ref class CardPermissionFlagValues abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type CardPermissionFlagValues = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardPermissionFlagValues
##  __Заметки
Константы лучше всего использовать для создания алгоритмов вычисления прав
доступа в классах вида
[ICardPermissionResolver](T_Tessa_Cards_ICardPermissionResolver.htm).
## __Поля
[AllCard](F_Tessa_Cards_CardPermissionFlagValues_AllCard.htm)|  Все разрешения
или запреты, допустимые для карточки.  
---|---  
[AllEntry](F_Tessa_Cards_CardPermissionFlagValues_AllEntry.htm)|  Все
разрешения или запреты, допустимые для строковой секции.  
[AllField](F_Tessa_Cards_CardPermissionFlagValues_AllField.htm)|  Все
разрешения или запреты, допустимые для поля.  
[AllFile](F_Tessa_Cards_CardPermissionFlagValues_AllFile.htm)|  Все разрешения
или запреты, допустимые для файла, прикреплённого к карточке.  
[AllowAllCard](F_Tessa_Cards_CardPermissionFlagValues_AllowAllCard.htm)|  Все
разрешения, допустимые для карточки.  
[AllowAllEntry](F_Tessa_Cards_CardPermissionFlagValues_AllowAllEntry.htm)|
Все разрешения, допустимые для строковой секции.  
[AllowAllField](F_Tessa_Cards_CardPermissionFlagValues_AllowAllField.htm)|
Все разрешения, допустимые для поля.  
[AllowAllFile](F_Tessa_Cards_CardPermissionFlagValues_AllowAllFile.htm)|  Все
разрешения, допустимые для файла, прикреплённого к карточке.  
[AllowAllRow](F_Tessa_Cards_CardPermissionFlagValues_AllowAllRow.htm)|  Все
разрешения, допустимые для строки.  
[AllowAllTable](F_Tessa_Cards_CardPermissionFlagValues_AllowAllTable.htm)|
Все разрешения, допустимые для коллекционной или древовидной секции.  
[AllRow](F_Tessa_Cards_CardPermissionFlagValues_AllRow.htm)|  Все разрешения
или запреты, допустимые для строки.  
[AllTable](F_Tessa_Cards_CardPermissionFlagValues_AllTable.htm)|  Все
разрешения или запреты, допустимые для коллекционной или древовидной секции.  
[DeleteCard](F_Tessa_Cards_CardPermissionFlagValues_DeleteCard.htm)|
Разрешение и запрет на удаление карточки:
[AllowDeleteCard](T_Tessa_Cards_CardPermissionFlags.htm) и
[ProhibitDeleteCard](T_Tessa_Cards_CardPermissionFlags.htm).  
[DeleteFile](F_Tessa_Cards_CardPermissionFlagValues_DeleteFile.htm)|
Разрешение и запрет на удаление файла:
[AllowDeleteFile](T_Tessa_Cards_CardPermissionFlags.htm) и
[ProhibitDeleteFile](T_Tessa_Cards_CardPermissionFlags.htm).  
[DeleteRow](F_Tessa_Cards_CardPermissionFlagValues_DeleteRow.htm)|  Разрешение
и запрет на удаление строки:
[AllowDeleteRow](T_Tessa_Cards_CardPermissionFlags.htm) и
[ProhibitDeleteRow](T_Tessa_Cards_CardPermissionFlags.htm).  
[EditNumber](F_Tessa_Cards_CardPermissionFlagValues_EditNumber.htm)|
Разрешение и запрет на редактирование номера:
[AllowEditNumber](T_Tessa_Cards_CardPermissionFlags.htm) и
[ProhibitEditNumber](T_Tessa_Cards_CardPermissionFlags.htm).  
[InsertFile](F_Tessa_Cards_CardPermissionFlagValues_InsertFile.htm)|
Разрешение и запрет на создание файла:
[AllowInsertFile](T_Tessa_Cards_CardPermissionFlags.htm) и
[ProhibitInsertFile](T_Tessa_Cards_CardPermissionFlags.htm).  
[InsertRow](F_Tessa_Cards_CardPermissionFlagValues_InsertRow.htm)|  Разрешение
и запрет на добавление строки:
[AllowInsertRow](T_Tessa_Cards_CardPermissionFlags.htm) и
[ProhibitInsertRow](T_Tessa_Cards_CardPermissionFlags.htm).  
[Modify](F_Tessa_Cards_CardPermissionFlagValues_Modify.htm)|  Разрешение и
запрет на изменение: [AllowModify](T_Tessa_Cards_CardPermissionFlags.htm) и
[ProhibitModify](T_Tessa_Cards_CardPermissionFlags.htm).  
[ProhibitAllCard](F_Tessa_Cards_CardPermissionFlagValues_ProhibitAllCard.htm)|
Все запреты, допустимые для карточки.  
[ProhibitAllEntry](F_Tessa_Cards_CardPermissionFlagValues_ProhibitAllEntry.htm)|
Все запреты, допустимые для строковой секции.  
[ProhibitAllField](F_Tessa_Cards_CardPermissionFlagValues_ProhibitAllField.htm)|
Все запреты, допустимые для поля.  
[ProhibitAllFile](F_Tessa_Cards_CardPermissionFlagValues_ProhibitAllFile.htm)|
Все запреты, допустимые для файла, прикреплённого к карточке.  
[ProhibitAllRow](F_Tessa_Cards_CardPermissionFlagValues_ProhibitAllRow.htm)|
Все запреты, допустимые для строки.  
[ProhibitAllTable](F_Tessa_Cards_CardPermissionFlagValues_ProhibitAllTable.htm)|
Все запреты, допустимые для коллекционной или древовидной секции.  
[ReplaceFile](F_Tessa_Cards_CardPermissionFlagValues_ReplaceFile.htm)|
Разрешение и запрет на замену файла:
[AllowReplaceFile](T_Tessa_Cards_CardPermissionFlags.htm) и
[ProhibitReplaceFile](T_Tessa_Cards_CardPermissionFlags.htm).  
[SignFile](F_Tessa_Cards_CardPermissionFlagValues_SignFile.htm)|  Разрешение и
запрет на подписание файла:
[AllowSignFile](T_Tessa_Cards_CardPermissionFlags.htm) и
[ProhibitSignFile](T_Tessa_Cards_CardPermissionFlags.htm).  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
